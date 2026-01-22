import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import numpy    as np
import pandas	as pand

from describe import describeFeature
from describe import printFeatures

def createTeta(house:array):
	teta = [0, 0, 0, 0, 0, 0, 0, 0, 0]

	for eleve in house:
		formula = 0
		for it, mat in enumerate(eleve):
			if type(mat) == float and not math.isnan(mat):
				formula += teta[it] * mat
		print(formula)

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

	#
	# Creation de houseMap
	houseMap = {}
	for value in dataFieldTrain.values:
		house = value[0]

		if house not in houseMap:
			houseMap[house] = []
		houseMap[house].append(value)

	for key, value in houseMap.items():
		createTeta(value);
		break
	#calcul = value_Astro * TetaAstro + 

#
# Main guard
if __name__ == "__main__":
	main();