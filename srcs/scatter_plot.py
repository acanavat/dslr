import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import numpy	as np
import pandas	as pand

from utils		import softmax
from describe 	import describeFeature
from describe 	import printFeatures

#
# main
def main():
	# Parsing en utilisant 'argparse'
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	# Extraction du dataset et des valeurs de describe
	dataField			= pand.read_csv(args.datasetPath)
	describeFeatureArr	= dataField.apply(describeFeature);
	describeFeatureLeg	= describeFeature(None);

	# Creation du graph
	classNameArr		= [];
	xTickArr			= [];
	yTickArr			= [];

	for value in describeFeatureArr:
		if value is None:
			continue
		xTick = value[2];
		yTick = value[3];
		plt.scatter(xTick, yTick, s=15)

		classNameArr.append(value[0]);
		xTickArr.append(xTick);
		yTickArr.append(yTick);

	# Affichage du graph
	plt.xlabel("mean")
	plt.xticks(xTickArr, classNameArr, rotation=45)
	plt.ylabel("std")
	# plt.yticks(yTickArr, classNameArr, rotation=0)
	plt.show()

#
# Main guard
if __name__ == "__main__":
	main();