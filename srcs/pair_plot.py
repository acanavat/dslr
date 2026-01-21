import csv
import math
import array
import argparse

import seaborn				as sns
import matplotlib.pyplot	as plt
import numpy				as np
import pandas				as pand

from describe import describeFeature
from describe import printFeatures

#
# main
def main():
	# Parsing en utilisant 'argparse'
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	# Extraction du dataset et des valeurs de describe
	dataField			= pand.read_csv(args.datasetPath)
	dataFieldDefinitive	= pand.DataFrame()
	# penguins			= sns.load_dataset(args.datasetPath)
	
	for key, value in dataField.items():
		if key == "Hogwarts House":
			dataFieldDefinitive[key] = value;
		if (value.dtype != np.float64):
			continue;
		dataFieldDefinitive[key] = value;

	print(dataFieldDefinitive);

	sns.pairplot(pand.DataFrame(dataFieldDefinitive), hue="Hogwarts House")
	plt.show()


#
# Main guard
if __name__ == "__main__":
	main();