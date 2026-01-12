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

