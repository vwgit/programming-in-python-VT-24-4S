import math

def fact(n):
	if n == 1:
		return 1
	if n == 0:
		return 1
	return fact(n) * fact(n - 1)

def recursion(i, n):
	if i == n:
		return x**i / (math.sqrt(fact(i) + i ** 3))
	return recursion(i + 1, n)

print(recursion(1, 5)