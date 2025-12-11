import math

def stepen(x, i):
	if i == 0:
		return 1
	return x * stepen(x, i-1)

def sum_recursive(x, i):
	if i == 0:
		return 0
	return stepen(x, i) /(stepen(math.e, stepen(i, 2)) + sum_recursive(x, i-1))

print("Получившиеся сумма: ", sum_recursive(2, 2))