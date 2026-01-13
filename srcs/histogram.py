import csv
import array
import argparse
import matplotlib
import matplotlib.pyplot as plt
import pandas as pand


#
# main
def main():
	# Parsing en utilisant 'argparse'
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	# Extraction du dataset

	dataField	= pand.read_csv(args.datasetPath);

	#
	# Print
	houses = getHouseMap(dataField);
	for house in houses:
		print ("__ {}".format(house))
		test = [row["Divination"] for row in houses[house] if pand.notnull(row["Divination"])]
		plt.hist(tuple(test))
	plt.show()

def getHouseMap(dataField : pand.core.frame.DataFrame) -> {}:
	houseMap = {};
	for index, row in dataField.iterrows():
		if (row is None):
			continue ;

		key = row['Hogwarts House']
		if key not in houseMap:
			houseMap[key] = [];
		houseMap[key].append(row);
	return (houseMap);


#
# Main guard
if __name__ == "__main__":
	main();
