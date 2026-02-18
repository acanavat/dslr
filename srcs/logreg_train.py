import os
import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import numpy    as np
import pandas	as pand

from utils			import mean
from utils			import getTableMat
from describe		import printFeatures
from describe		import describeFeature
from utils_softmax	import softmax
from utils_softmax	import normalizeDatafield


def replaceNanInArr(array: list) -> list:
	for index, nanFinder in enumerate(array[1:]):
		if math.isnan(nanFinder):
			array[index + 1] = 0;
	return(array)


def createTeta(ds: pand.Series) -> list :
	# tetaArr = [[]];
	# [eleve1[zouk, afro dance, politique]
	#   eleve2[...]]
	#	E eleveX[1] 

	#
	# Normalisation des valeurs
	ds = normalizeDatafield(ds)

	#
	# Le training
	learning8rate	= 0.01
	nbEpoch			= 1;

	tetas = np.zeros([ds["Hogwarts House"].nunique(), ds.shape[1] - 1])
	if (not len(tetas)):
		print(f"Error, 'Hogwarts House' key seems empty")
		return ([]);

	houseIndex = {}
	for i, house in enumerate(ds["Hogwarts House"].unique()):
		houseIndex[house] = i
	houseSerie = ds["Hogwarts House"];

	scoreArray = [[]];
	scoreArray = np.zeros([ds["Hogwarts House"].nunique(), 0])
	for epoch in range(nbEpoch):
		total_loss = 0
		n_samples = 0
		for value in ds.values:
			replaceNanInArr(value)
			result = [];
			for tetaHouse in tetas:
				result.append(np.dot(value[1:], tetaHouse))

			proba = softmax(np.asarray(result, dtype=np.float32), 0)

			loss = -np.log(proba[houseIndex[value[0]]] + 1e-15)
			total_loss += loss
			# print(f"DEBUG proba: {proba}")
			# print(f"DEBUG sum proba: {np.sum(proba)}")  # DOIT = 1.0
			# print(f"DEBUG true proba: {proba[houseIndex[value[0]]]}")  # DOIT être 0→1

			gradient = proba.copy()
			gradient[houseIndex[value[0]]] -= 1

			x = value[1:]
			for k in range(len(tetas)):
				tetas[k] = tetas[k].astype(np.float64) - learning8rate * gradient[k] * x
			n_samples += 1
		# print(f"EPOCH TERMINÉE - Perte moyenne: {total_loss/n_samples:.3f}")

	tetaDict = {}
	for i, house in enumerate(houseIndex):
		tetaDict[house] = tetas[i];
		print(house, ":", tetas[i])
	return(tetaDict);

#
# main
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	#
	# Creation de dataFieldTrain
	try:
		dataField	= pand.read_csv(args.datasetPath)
		tabMat		= getTableMat()

		dataFieldTrain	= pand.DataFrame({key:value for key, value in dataField.items() if key in tabMat})
	except Exception as e:
		print(f"{type(e).__name__} : {e}")
		return ;

	#
	# On appelle la fonction de learn
	tetaDict = createTeta(dataFieldTrain)
	if (not len(tetaDict)):
		return ;

	#
	# mettre les resultats dans le fichier
	if os.path.exists("teta/brain.csv"):
		os.remove("teta/brain.csv")

	with open("teta/brain.csv", "a") as file:
		# CSV Header
		for index, mat in enumerate(tabMat):
			if (index == 0):
				file.write(f"House Name,")
				continue ;
			# file.write(f"teta{index - 1}")
			file.write(f"{mat}")
			if (index < len(tabMat) - 1):
				file.write(",")
		file.write("\n")

		# Values
		for house, teta in tetaDict.items():
			file.write(f"{house},")
			for index, element in enumerate(teta):
				file.write(f"{element}")
				if (index < len(teta) - 1):
					file.write(",")
			file.write("\n")
	
#
# Main guard
if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"{type(e).__name__} : {e}")
	except KeyboardInterrupt:
		print("");
