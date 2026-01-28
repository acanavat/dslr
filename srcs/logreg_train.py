import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt
import os

import numpy    as np
import pandas	as pand
from utils 	  import mean
from describe import describeFeature
from describe import printFeatures

def createTeta(house: array, feature: pand.Series, houseName : str = "default"):
	teta = [0, 0, 0, 0, 0, 0, 0, 0]
	x = -1
	for key, value in feature.items():
		x += 1
		if key == "Hogwarts House":
			continue
		for eleve in house:
			if type(eleve[x]) == float and not math.isnan(eleve[x]):
				eleve[x] = (eleve[x] - value[2]) / value[3]
	learning_rate = 0.001
	
	for epoch in range(1000):
		cost = 0
		false = 0
		for eleve in house:
			prediction = 0
			for it, mat in enumerate(eleve):
				if type(mat) == np.float64 and not math.isnan(mat):
					prediction += teta[it - 1] * mat
			exp = math.exp(-prediction)
			#maintenant on determine (pour la maison) si la prediction de la matiere vaut 0 ou 1 et en fonction on applique la formule 
			sigmoide = 1 / (1 + exp)
			if sigmoide > 0.5:
				cost += -math.log(sigmoide)
			else:
				cost += -math.log(1 - sigmoide)
				false += 1
			error = sigmoide - 1
			for it, mat in enumerate(eleve):
				if type(mat) == np.float64 and not math.isnan(mat):
					teta[it - 1] -= learning_rate * error * mat
	with open("teta/brain", "a") as file:
		file.write(f"{houseName} : {teta}")
		error_rate = false / len(house)
		j = 1/len(house) * cost
	print(f"Epoch {epoch}: J={j:.3f}, Err={error_rate:.1%}, teta={teta}...")

def handleTetaStudent(tetaArr:array, newStud:array):
	print("on gere ", newStud, "tetas =", tetaArr)

		# init a 0
	


#
# main

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	#
	# Creation de dataFieldTrain
	dataField	= pand.read_csv(args.datasetPath)
	tabMat = [
				"Hogwarts House", "Astronomy", "Herbology"
				"Divination", "Muggle Studies", "Ancient Runes",
				"History of Magic", "Transfiguration", "Charms",
				"Flying", "Defense Against the Dark Arts"
			]

	dataFieldTrain = pand.DataFrame({key:value for key, value in dataField.items() if key in tabMat})

	described = dataFieldTrain.apply(describeFeature)
	# described['Hogwarts House'] = dataFieldTrain['Hogwarts House']
	# printFeatures(describeFeature(None), described)
	# print(described)

	#
	# Creation de houseMap
	houseMap = {}
	for value in dataFieldTrain.values:
		house = value[0]

		if house not in houseMap:
			houseMap[house] = []
		houseMap[house].append(value)
	if os.path.exists("teta/brain"):
		os.remove("teta/brain")
	for key, value in houseMap.items():
		print("on gere la maison", key)
		createTeta(value, described, key)
	#calcul = value_Astro * TetaAstro + 

#
# Main guard
if __name__ == "__main__":
	main();