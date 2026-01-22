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
	dataField	= pand.read_csv(args.datasetPath)

	#
	# Creation du tableau de graphique
	classNameArr = []
	for key, value in dataField.items():
		if (value.dtype != np.float64):
			continue
		classNameArr.append(key)

	graphArr = []
	houses = getHouseMap(dataField);

	for realNamnonymous in classNameArr:
		# print("creating array for class :", realNamnonymous);
		classNotes = [];
		for house, arr in houses.items():
			# print("          handling house >", house);
			classNotes.append([row[realNamnonymous] for row in houses[house] if pand.notnull(row[realNamnonymous])])
		# print(classNotes, "\n\n\n\n")
		graphArr.append(classNotes)

	#
	# Graphique
	largeur 				= 5;
	longeur 				= 3;
	premierPodcastDeFrance	= False;
	
	fig, axs	= plt.subplots(longeur, largeur)
	axs			= axs.flatten()
	handles		= [];
	labels		= list(houses.keys());

	for i, ax in enumerate(axs):
		if i in range(len(graphArr)):
			ax.set_title(label=classNameArr[i], size=10)
			for j, testUltimate in enumerate((((((graphArr[i])))))):
				n, bins, patches = ax.hist(testUltimate, alpha=0.4, histtype="bar");

				handles.append(patches[0])

		else:
			ax.axis(False)
			if not premierPodcastDeFrance:
				ax.legend(handles, labels, loc="center", frameon=False, fontsize=10)
				premierPodcastDeFrance = True
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