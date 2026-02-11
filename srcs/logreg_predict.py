import os
import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import numpy		as np
import pandas		as pand

from utils		import mean
from utils		import getTableMat
from describe	import describeFeature
from describe	import printFeatures

def prediction(dataPrediction, tetaHouse):
	best_sigmoide		= {}
	goodPredictions		= {}
	badPredictions		= {}
	globalPredictions	= {}

	# describeFeatureArr	= dataPrediction.apply(describeFeature);
	
	for elevePredict in dataPrediction.values:
		for teta in tetaHouse.values:
			predict = 0
			for small_student, small_teta, i in zip(elevePredict[1:], teta[1:], range(1, len(teta[1:]))): 
				if not math.isnan(small_student):
					predict += small_student * small_teta
				# else:
				# 	predict += describeFeatureArr[i][2] * small_teta;
					# Code pour ajouter la moyenne

			best_sigmoide[teta[0]] = predict
		
		predictedHouse = max(best_sigmoide, key=best_sigmoide.get)

		if predictedHouse not in globalPredictions:
			globalPredictions[predictedHouse] = [];
		globalPredictions[predictedHouse].append(best_sigmoide);

		if type(elevePredict[0]) == str:
			if elevePredict[0] not in goodPredictions:
				goodPredictions[elevePredict[0]] = 0
			if elevePredict[0] not in badPredictions:
				badPredictions[elevePredict[0]] = 0

			if elevePredict[0] == max(best_sigmoide, key=best_sigmoide.get):
				goodPredictions[elevePredict[0]] += 1
			else:
				print(f"{elevePredict[0]} [{predictedHouse}]\t: {best_sigmoide}")
				badPredictions[elevePredict[0]] += 1

	print(f"good : {goodPredictions}")
	print(f"bad  : {badPredictions}")
	print(f"Gryffindor  : {len(globalPredictions['Gryffindor'])}")
	print(f"Hufflepuff  : {len(globalPredictions['Hufflepuff'])}")
	print(f"Ravenclaw   : {len(globalPredictions['Ravenclaw'])}")
	print(f"Slytherin   : {len(globalPredictions['Slytherin'])}")

#
# Main
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	#
	# Creation de dataFieldPrediction
	dataField			= pand.read_csv(args.datasetPath)
	tabMat				= getTableMat();
	dataFieldPrediction = pand.DataFrame({key:value for key, value in dataField.items() if key in tabMat})

	with open("teta/brain.csv", "r") as file:
		tetaHouse = pand.read_csv("teta/brain.csv")
	prediction(dataFieldPrediction, tetaHouse)

if __name__ == "__main__":
	main()