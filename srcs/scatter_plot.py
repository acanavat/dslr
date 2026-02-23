import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import numpy	as np
import pandas	as pand

from describe		import describeFeature
from describe		import printFeatures
from utils_softmax	import normalizeDatafield

#
# main
def main():
	# Parsing en utilisant 'argparse'
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	# Extraction du dataset et des valeurs de describe
	try:
		dataField			= pand.read_csv(args.datasetPath)
		describeFeatureArr	= dataField.apply(describeFeature)
		# dataField			= normalizeDatafield(dataField)
		describeFeatureLeg	= describeFeature(None)
	except Exception as e:
		print(f"{type(e).__name__} : {e}")
		return

	# Creation du graph
	classNameArr		= []
	xTickArr			= []
	yTickArr			= []

	for value in describeFeatureArr:
		if value is None or not len(value):
			continue
		xTick = value[2]
		yTick = value[3]
		plt.scatter(xTick, yTick, s=15)

		classNameArr.append(value[0])
		xTickArr.append(xTick)
		yTickArr.append(yTick)

	# print(dataField)
	# for it in dataField.items():
		# key		= it[0]
		# feature	= it[1]
		# if (feature.dtype != np.float64):
			# continue
		# print(f"{feature.values}")
		# for note in feature:
			# plt.scatter(note, note, s=15)

	# Affichage du graph
	plt.xlabel("mean")
	plt.xticks(xTickArr, classNameArr, rotation=45)
	plt.ylabel("std")
	# plt.yticks(yTickArr, classNameArr, rotation=0)
	plt.show()

#
# Main guard
if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"{type(e).__name__} : {e}")
	except KeyboardInterrupt:
		print("")
