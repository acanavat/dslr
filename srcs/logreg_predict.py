import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt
import os

import numpy	as np
import pandas	as pand
from utils		import mean
from describe	import describeFeature
from describe	import printFeatures

def prediction(dataPrediction, tetaHouse):
	best_sigmoide	= {}
	goodPredictions	= {}
	badPredictions	= {}

	describeFeatureArr	= dataPrediction.apply(describeFeature);
	printFeatures(describeFeature(None), describeFeatureArr)
	# print(describeFeatureArr[2]);
	
	#message pour isibio : et si quand une valeur est null on prenait la moyenne de la valeur de la maison (peut etre un bon truc)
	for elevePredict in dataPrediction.values:
		# print(f"\n\nle eleve = {elevePredict}")
		for teta in tetaHouse.values:
			predict = 0
			#print(f"On gere: {teta[0]}")
			for small_student, small_teta, i in zip(elevePredict[1:], teta[1:], range(1, len(teta[1:]))): 
				# print(f"gogogo = {small_student}")
				# print("test : ", teta)
				if not math.isnan(small_student):
					predict += small_student * small_teta
				else:
					# print("mat =", describeFeatureArr[i][2])
					# print("fdp de i =", i)
					predict += describeFeatureArr[i][2] * small_teta;
					predict += 10000000000;
			#print(f"toujours la forme \033[5m{predict}")
			best_sigmoide[teta[0]] = predict
		
		predictedHouse = max(best_sigmoide, key=best_sigmoide.get)
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
#
# Main
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	#
	# Creation de dataFieldPrediction
	dataField	= pand.read_csv(args.datasetPath)
	# tabMat = [
	# 			"Hogwarts House", "Astronomy", "Herbology",
	# 			"Divination", "Muggle Studies", "Ancient Runes",
	# 			"History of Magic", "Transfiguration", "Charms",
	# 			"Flying", "Defense Against the Dark Arts"
	# 		]
	tabMat = [
				"Hogwarts House", "Astronomy", "Potions",
				"Divination", "Muggle Studies", "Ancient Runes",
				"History of Magic", "Transfiguration", "Charms",
				"Flying", "Defense Against the Dark Arts"
			]
	# tabMat = [
	# 			"Hogwarts House",
	# 			"Divination", "Muggle Studies", "Ancient Runes",
	# 			"History of Magic", "Transfiguration", "Charms",
	# 			"Flying"
	# 		]

	dataFieldPrediction = pand.DataFrame({key:value for key, value in dataField.items() if key in tabMat})

	
	houseMap = {}
	with open("teta/brain.csv", "r") as file:
		tetaHouse = pand.read_csv("teta/brain.csv")
	prediction(dataFieldPrediction, tetaHouse)
if __name__ == "__main__":
	main()