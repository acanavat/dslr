import os
import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import numpy		as np
import pandas		as pand

from utils			import mean
from utils			import softmax
from utils			import getTableMat
from utils			import normalizeDatafield
from describe		import printFeatures
from describe		import describeFeature
from logreg_train	import replaceNanInArr

def prediction(dataPrediction, tetaHouse):
	#
	# Preparation des tableaux pour le dot product

	# dataPrediction :	on remove la colonne 'Hogwarts House'
	# 					on normalise les valeurs car il faut utiliser les valeurs comme au training, or,
	#					au training les valeurs ont ete normalises
	dataPredictionForPredict = dataPrediction.drop("Hogwarts House", axis='columns')
	dataPredictionForPredict = normalizeDatafield(dataPredictionForPredict)

	# tetaHouse :	- on doit reformer le tableau et passer de
	#				[nb classes : nb features] a [nb features : nb classes]
	#				- on en profite pour creer `houseIndexDict` qui va nous permettre
	#				d'interpreter les resultats de sortie de softmax
	tetaArrReshaped	= [[]];
	houseIndexDict	= {}

	for houseIndex, value in enumerate(tetaHouse.values):
		for tetaIndex, teta in enumerate(value[1:]):
			if len(tetaArrReshaped) <= tetaIndex:
				tetaArrReshaped.append([]);
			tetaArrReshaped[tetaIndex].append(teta)

		houseIndexDict[houseIndex] = value[0]

	# print(f"houseIndexDict:\n{houseIndexDict}");
	# print(f"tetaArrReshaped norm:\n{np.linalg.norm(tetaArrReshaped)}");

	#
	# Calculs de prediction avec softmax
	dot_result		= np.dot(np.nan_to_num(dataPredictionForPredict), tetaArrReshaped)
	softmax_result	= softmax(dot_result, 1)
	predict			= np.argmax(softmax_result, axis=1)

	# print(f"predict:\n{predict}");
	# print(f"sum of softmax results:\n{np.sum(softmax_result, axis=1)}");

	#
	# Traitement des resultats de prediction
	goodPredictions		= {}
	badPredictions		= {}
	predictionList		= [];

	for studentIndex, predictedHouse in enumerate(predict):
		predictedHouseStr	= houseIndexDict[predictedHouse];
		predictionList.append(predictedHouseStr)

		# comptage des erreurs (si le dataset fournit les maisons correctes)
		correctHouseStr		= dataPrediction.values[studentIndex][0];

		if type(correctHouseStr) == str:
			if predictedHouseStr not in goodPredictions:
				goodPredictions[predictedHouseStr] = 0
			if predictedHouseStr not in badPredictions:
				badPredictions[predictedHouseStr] = 0

			if predictedHouseStr == correctHouseStr:
				goodPredictions[predictedHouseStr] += 1
			else:
				print(f"bad prediction ({predictedHouseStr}!={correctHouseStr})")
				badPredictions[predictedHouseStr] += 1

	#
	# Affichage des predictions (si le dataset fournit les maisons correctes)
	if goodPredictions:
		print(f"good : {goodPredictions}")
	if badPredictions:
		print(f"bad  : {badPredictions}")

	#
	# Return des resultats
	return (predictionList);

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

	#
	# Appel de la fonctiond de prediction
	predictionList = prediction(dataFieldPrediction, tetaHouse)

	#
	# Sauvegarde des resultats dans un fichier
	if os.path.exists("teta/houses.csv"):
		os.remove("teta/houses.csv")

	with open("teta/houses.csv", "a") as file:
		# CSV Header
		file.write(f"Index,Hogwarts House\n")

		# Values
		for index, house in enumerate(predictionList):
			file.write(f"{index},{house}\n")

if __name__ == "__main__":
	main()