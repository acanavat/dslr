import csv
import math
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
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
	describe	= dataField.apply(describeFeature);

	# stdArr		= [];
	# for key, value in describe.items():
	# 	if (value is None):
	# 		continue
	# 	std = value[3]
	# 	stdArr.append(std)
	# print(stdArr);
	# plt.hist(stdArr)
	# plt.autoscale(axis='x')
	# plt.tight_layout()
	# plt.show()

	#
	# PRINT V2
	# perfect = {}
	# for key, value in df.items():
	# 	if (value.dtype != np.float64):
	# 		continue ;
	# 	if key not in perfect:
	# 		perfect[key] = [];
	# 	perfect[key].append(value)

	# # 	perfect = [magical for magical in arr if arr["Arithmancy"]]
	# # print(perfect)
	# 	return ;



	# -- PRINT V1 : NE MARCHE QUE POUR UNE MATIERE
	houses		= getHouseMap(dataField);
	finalArr	= {};
	for house, arr in houses.items():
		print("__ {}".format(house))
		df			= pand.DataFrame(arr)

		finalDict	= {};
		for name, course in df.items():
			if (course.dtype != np.float64):
				continue ;
			print("GAY:", name)

			if name not in finalDict:
				finalDict[name] = [];
			finalDict[name].append(row for row in course if pand.notnull(row));
		
		if house not in finalArr:
			finalArr[house] = [];
		finalArr[house].append(finalDict);

	print(finalArr);

	for testUltimate, untimateUltimate in finalArr.items():
		for theFinalUltimate in untimateUltimate:
			for absoluteDictKey, absoluteDictValye in theFinalUltimate.items():
				print(absoluteDictKey, "->", absoluteDictValye)
				plt.hist(finalDict, alpha=0.5)
		plt.show()




		# printable	= df.apply(describeFeature);
		# printFeatures(describeFeature(None), printable);

def getHouseMap(dataField : pand.core.frame.DataFrame) -> {}:
	houseMap = {}
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
