import csv
import argparse

from dataclasses import dataclass, field

@dataclass
class Feature:
    name: str
    values: list = field(default_factory=list)

#
# main
def main():
	# Parsing en utilisant 'argparse'
	parser = argparse.ArgumentParser()
	parser.add_argument("datasetPath", type=str)
	args = parser.parse_args()

	# Extraction du dataset
	dataset = getCsvAsList(args.datasetPath);
	print("gay test = {}".format(dataset[0]));

	# Creation des features (type Feature)

#
# Utils
def getCsvAsList(csvFilePath : str):
	# params:
	#	- csvFilePath : path du fichier '.csv'
	#
	# Ouvre le fichier passe en argument, utilise 'csv.reader' pour creer un objet reader
	# et enfin return cet objet sous forme de liste

	csvAsList = [];

	with open(csvFilePath) as csvFile:
		csvReaderObject		= csv.reader(csvFile);
		csvAsList			= list(csvReaderObject);
	return list(csvAsList);

# def getFeatures(dataset : list[str]):


#
# Main guard
if __name__ == "__main__":
	main();
