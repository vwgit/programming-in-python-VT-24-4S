import math

def fact(n):
	if n == 1:
		return 1
	if n == 0:
		return 1
	return fact(n - 1)

def recursion(i, n, x):
	if i == n:
		return x**i / (math.sqrt(fact(i) + i ** 3))
	return recursion(i + 1, n, x)

x = int(input("Введите число x: "))
i = int(input("Введите число i: "))
n = int(input("Введите число n: "))
print(recursion(i, n, x))