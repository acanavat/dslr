import csv
import argparse
import math
import numpy as np
import pandas as pand
import statistics
from pprint import pprint

import utils
from dataclasses import dataclass, field

#
# main
def main():
	# Parsing en utilisant 'argparse'
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	# Extraction du dataset
	dataField			= pand.read_csv(args.datasetPath);
	describeFeatureArr	= dataField.apply(describeFeature);
	printFeatures(describeFeatureArr);


	# Creation des features (type Feature)

#
# Utils
def describeFeature(feature : pand.Series) -> list :

	# Tester si la feature est bien numerique

	if (feature.dtype != np.float64):
		return ;

	# print("\n---\n");
	# print("feature : {}".format(feature.name))
	# print("        : {}".format(feature.values))
	# print("        : {}".format(feature.dtype))
	# print("        : {}".format(type(feature.values[0])))

	arrayClean = [value for value in feature.values if not math.isnan(value)];
	arrayClean.sort()

	arrayResult = [
		feature.name,
		len(arrayClean),
		utils.mean(arrayClean),
		utils.std(arrayClean),
		min(arrayClean),
		utils.quartile(arrayClean, 1),
		utils.quartile(arrayClean, 2),
		utils.quartile(arrayClean, 3),
		max(arrayClean)];

	# print("arrayResult  {}".format(arrayResult))

	# print("count  {}".format(len(arrayClean)))
	# print("mean   {}".format(utils.mean(arrayClean)))
	# print("std    {}".format(utils.std(arrayClean)))
	# print("min    {}".format(min(arrayClean)))
	# print("25%    {}".format(utils.quartile(arrayClean, 1)))
	# print("50%    {}".format(utils.quartile(arrayClean, 2)))
	# print("75%    {}".format(utils.quartile(arrayClean, 3)))
	# print("max    {}".format(max(arrayClean)))

	return (arrayResult);

def printFeatures(featureArr):

	print(featureArr);

	#
	# Check que tous les tableaux sont de la meme taille
	arrLen = 0;
	for row in featureArr:
		if (not row):
			continue ;
		if (arrLen and arrLen != len(row)):
			print ("erreur taile tableau, tous les elements sous tableaux doivent etre de taille egale")
			return ;
		elif (not arrLen):
			arrLen = len(row)

	#
	# Creation du tableau pour print
	for i in range(arrLen):
		printLine = [];
		for row in featureArr:
			if (not row):
				continue ;
			printLine.append(row[i]);
		print("  ".join(f"{element:>20}" for element in printLine))
		# print(printLine);

def pandasSerieToList(serie : pand.Series) -> list :
	return serie.tolist()

#
# Main guard
if __name__ == "__main__":
	main();
