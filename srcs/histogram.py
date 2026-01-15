import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt

import numpy	as np
import pandas	as pand

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
	name = []
	for key, value in dataField.items():
		if (value.dtype != np.float64):
			continue
		name.append(key)
	p = 10
	for i in name:
		if (len(name) % p) == 0:
			break
		p -= 1

	largeur = 5;
	longeur = 3;


	fig, axs = plt.subplots(longeur, largeur)
	axs = axs.flatten()

	newTest = []
	houses = getHouseMap(dataField);

	for realNamnonymous in name:
		test = [];
		for house, arr in houses.items():
			test.append([row[realNamnonymous] for row in houses[house] if pand.notnull(row[realNamnonymous])])
		newTest.append(test)

	for i, ax in enumerate(axs):
		if i in range(len(newTest)):
			ax.set_title(label=name[i])
			for testUltimate in newTest[i]:
				ax.hist(testUltimate, alpha=0.5);
		else:
			ax.axis(False)
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