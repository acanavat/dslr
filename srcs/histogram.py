import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import pandas as pand

from describe import describeFeature
from describe import printFeatures

#
# main
def main():
	# Parsing en utilisant 'argparse'
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()
	
	#
	# Extraction du dataset
	dataField	= pand.read_csv(args.datasetPath);

	#
	# Print
	houses = getHouseMap(dataField);
	for house, arr in houses.items():
		print("__ {}".format(house))
		test = [row["Care of Magical Creatures"] for row in houses[house] if pand.notnull(row["Care of Magical Creatures"])]

		df			= pand.DataFrame(arr)
		printable	= df.apply(describeFeature);
		printFeatures(describeFeature(None), printable);

		plt.hist(test, alpha=0.5)
	plt.show()

def getHouseMap(dataField : pand.core.frame.DataFrame) -> {}:
	houseMap = {};
	for index, row in dataField.iterrows():
		if (row is None):
			continue ;

		#
		# Recuperation de la key et check qu'elle ne soit pas null
		key = row['Hogwarts House']
		if (type(key) is not str and math.isnan(key)):
			continue ;

		if key not in houseMap:
			houseMap[key] = [];
		houseMap[key].append(row);
	return (houseMap);

#
# Main guard
if __name__ == "__main__":
	main();
