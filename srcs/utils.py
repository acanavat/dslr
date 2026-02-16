import math

import numpy	as np
import pandas	as pand

from describe	import describeFeature


def mean(ave: list):
	return (sum(ave) / len(ave))


def variance(numbers):
	gap = [number - mean(numbers) for number in numbers]
	square = sum(x**2 for x in gap)
	return (square / (len(numbers)))


def std(numbers):
	return pow(variance(numbers), 0.5)

def quartile(numbers, quartile):
	if quartile == 1:
		return float(numbers[int(len(numbers) / 4)]) 
	if quartile == 2:
		return float(numbers[int(len(numbers) / 2)])
	if quartile == 3:
		return float(numbers[int(len(numbers) - (len(numbers) / 4))])

def getTableMat():
	return (
		[
			"Hogwarts House",
		
			# Ravensclaw a part
				"Muggle Studies",
				"Charms",
			# Slytherin a part
				# "Divination",
			# Gryffindor a part
				"History of Magic",
				# "Transfiguration",
				"Flying",
			# 50 / 50
				"Astronomy",
				# "Herbology",
				"Defense Against the Dark Arts",
				"Ancient Runes",
			# Mixed
				# "Arithmancy",
				"Potions",
				"Care of Magical Creatures"
		]);

def softmax(z, axis):
	#
	# Version from github pour tester :

	# you basically take the maximum of score and substract it with all other scores for numerical stability
	z = z - np.max(z, axis=axis, keepdims=True)

	# You then take exponent of scores since its negative and sum it along each row 
	# You then divide each row with its transposed exponent to normalize it and transpose it back to give its original shape
	softmax_out = (np.exp(z).T / np.sum(np.exp(z), axis=axis)).T 

	return softmax_out

	#
	# Version maison :

	# z est un vecteur de scores, par ex. result
	z = np.array(z)
	z_stable = z - np.max(z)      # stabilité numérique
	exp_z = np.exp(z_stable)
	# print("PUTANG", exp_z / np.sum(exp_z))
	return exp_z / np.sum(exp_z)

def normalizeDatafield(df: pand.core.frame.DataFrame):
	described	= df.apply(describeFeature)
	for key in df.columns:
		if key == "Hogwarts House":
			continue

		mean = described[key][2]
		std = described[key][3]

		# .loc pour modifier en place
		df.loc[:, key] = df[key].apply(lambda note: 
			(note - mean) / std if not math.isnan(note) else 0
		)
	return (df)