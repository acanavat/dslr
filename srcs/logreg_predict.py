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

def prediction(dataPrediction, tetaHouse):
	for key, value in dataPrediction.items():
		print(value[1])
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	#
	# Creation de dataFieldPrediction
	dataField	= pand.read_csv(args.datasetPath)
	tabMat = [
				"Hogwarts House", "Astronomy", "Herbology"
				"Divination", "Muggle Studies", "Ancient Runes",
				"History of Magic", "Transfiguration", "Charms",
				"Flying", "Defense Against the Dark Arts"
			]

	dataFieldPrediction = pand.DataFrame({key:value for key, value in dataField.items() if key in tabMat})

	described = dataFieldPrediction.apply(describeFeature)
	
	houseMap = {}
	with open("teta/brain", "r") as file:
		tetaHouse = pand.read_csv("teta/brain")
	prediction(dataFieldPrediction, tetaHouse)		
if __name__ == "__main__":
	main();