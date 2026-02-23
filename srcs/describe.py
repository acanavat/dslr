import csv
import math
import utils
import argparse
import statistics

import numpy		as np
import pandas		as pand

from pprint			import pprint
from dataclasses	import dataclass, field

#
# main
def main():
	# Parsing en utilisant 'argparse'
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	#
	# Extraction du dataset
	try:
		dataField			= pand.read_csv(args.datasetPath)
		describeFeatureArr	= dataField.apply(describeFeature)
	except Exception as e:
		print(f"{type(e).__name__} : {e}")
		return

	#
	# Appel de describeFeature et affichage des resultats avec printFeatures
	describeFeatureLeg	= describeFeature(None)
	printFeatures(describeFeatureLeg, describeFeatureArr)

#
# Utils
def describeFeature(feature : pand.Series) -> list :

	#
	# Si None est passe en argument, on retourne la legende
	if (feature is None):
		return ([
			"name",
			"nb elements",
			"mean",
			"std",
			"min",
			"25%",
			"50%",
			"75%",
			"max"])

	#
	# Tester si la feature est bien numerique
	if (feature.dtype != np.float64):
		return


	# prints de debug
	if False:
		print("\n---\n")
		print("feature : {}".format(feature.name))
		print("        : {}".format(feature.values))
		print("        : {}".format(feature.dtype))
		print("        : {}".format(type(feature.values[0])))

	#
	# Extraction des valeurs de la feature
	arrayClean = [value for value in feature.values if not math.isnan(value)]
	arrayClean.sort()

	# Check si le tableau n'est pas vide
	if not len(arrayClean):
		return([])

	#
	# Execution des calculs dans le tableau 'arrayResult'
	arrayResult = [
		feature.name,
		len(arrayClean),
		utils.mean(arrayClean),
		utils.std(arrayClean),
		min(arrayClean),
		utils.quartile(arrayClean, 1),
		utils.quartile(arrayClean, 2),
		utils.quartile(arrayClean, 3),
		max(arrayClean)]

	# prints de debug
	if False:
		print("arrayResult  {}".format(arrayResult))
		print("count  {}".format(len(arrayClean)))
		print("mean   {}".format(utils.mean(arrayClean)))
		print("std    {}".format(utils.std(arrayClean)))
		print("min    {}".format(min(arrayClean)))
		print("25%    {}".format(utils.quartile(arrayClean, 1)))
		print("50%    {}".format(utils.quartile(arrayClean, 2)))
		print("75%    {}".format(utils.quartile(arrayClean, 3)))
		print("max    {}".format(max(arrayClean)))

	return (arrayResult)

def printFeatures(legend, featureArr, width = 16):
	# Check que tous les tableaux sont de la meme taille
	arrLen = 0
	for row in featureArr:
		if (row is None or not row):
			continue
		if (arrLen and arrLen != len(row)):
			print ("erreur taile tableau, tous les elements sous tableaux doivent etre de taille egale")
			return
		elif (not arrLen):
			arrLen = len(row)

	#
	# Creation du tableau pour print
	for i in range(arrLen):
		printLine = []
		for row in featureArr:
			if (not row):
				continue
			printLine.append(row[i])

		printStr = ""
		printStr += (f"{legend[i]:<{width}}")
		for element in printLine:
			if (type(element) == str):
				printStr += (f"{element:>{width}.14}")
			else:
				printStr += (f"{element:>{width}.8f}")
		print(printStr)

def pandasSerieToList(serie : pand.Series) -> list :
	return serie.tolist()

#
# Main guard
if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"{type(e).__name__} : {e}")
	except KeyboardInterrupt:
		print("")
