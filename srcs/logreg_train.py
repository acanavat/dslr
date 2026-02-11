import os
import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import numpy    as np
import pandas	as pand

from utils		import mean
from describe	import describeFeature
from describe	import printFeatures
from utils		import getTableMat


def createTeta(house: array, feature: pand.Series):
	teta = [0 for value in range(1, len(feature))]
	x = -1

	for key, value in feature.items():
		x += 1
		if key == "Hogwarts House":
			continue
		for eleve in house:
			if type(eleve[x]) == float and not math.isnan(eleve[x]):
				eleve[x] = (eleve[x] - value[2]) / value[3]
	learning_rate = 0.001
	
	for epoch in range(100):
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

	
	error_rate = false / len(house)
	j = 1/len(house) * cost
	print(f"Epoch {epoch}: J={j:.3f}, Err={error_rate:.2%}, teta=teta...")

	return (teta)

#
# main
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	#
	# Creation de dataFieldTrain
	dataField	= pand.read_csv(args.datasetPath)
	tabMat = getTableMat();

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

	tetaDict = {}
	for key, value in houseMap.items():
		print("on gere la maison", key)
		if key not in tetaDict:
			tetaDict[key] = []
		tetaDict[key] = createTeta(value, described)


	if os.path.exists("teta/brain.csv"):
		os.remove("teta/brain.csv")

	with open("teta/brain.csv", "a") as file:
		# CSV Header
		for index, mat in enumerate(tabMat):
			if (index == 0):
				file.write(f"House Name,")
				continue ;
			file.write(f"teta{index - 1}")
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
	main();