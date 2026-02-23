import math

import numpy	as np
import pandas	as pand

from describe	import describeFeature

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
		if (df[key].dtype != np.float64):
			continue
		if key == "Hogwarts House":
			continue

		mean = described[key][2]
		std = described[key][3]

		# .loc pour modifier en place
		df.loc[:, key] = df[key].apply(lambda note: 
			(note - mean) / std if not math.isnan(note) else 0
		)
	return (df)
