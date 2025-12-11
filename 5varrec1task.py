#5вар 1 задание
import math
def power(x, n):
	if n == 0:
		return 1
	return x * power(x, n - 1)

def rec_sum(x, n):
	if n == 0:
		return 0
	return power(x, n) /(power(math.e, power(n, 2)) + rec_sum(x, n - 1))
print(rec_sum(2, 3)) 