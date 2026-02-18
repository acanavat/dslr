import csv
import math
import array
import argparse

import numpy				as np
import pandas				as pand
import seaborn				as sns
import matplotlib.pyplot	as plt

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
	try:
		dataField			= pand.read_csv(args.datasetPath)
		dataFieldDefinitive	= pand.DataFrame()
	except Exception as e:
		print(f"{type(e).__name__} : {e}")
		return ;

	for key, value in dataField.items():
		if key == "Hogwarts House":
			houseArr = [];
			for house in value:
				if (type(house) is not str and math.isnan(house)):
					house = "No House" ;
				houseArr.append(house);
			dataFieldDefinitive[key] = houseArr;
			continue ;

		if (value.dtype != np.float64):
			continue;
		dataFieldDefinitive[key] = value;

	sns.pairplot(pand.DataFrame(dataFieldDefinitive), hue="Hogwarts House")
	plt.show()

#
# Main guard
if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"{type(e).__name__} : {e}")
	except KeyboardInterrupt:
		print("");
