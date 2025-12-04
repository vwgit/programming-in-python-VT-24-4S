import math

def fact(n):
	if n <= 1:
		return 1
	return n * fact(n-1)

def recursion(i, n, x, sum):
	if i == n:
		return x**i / (math.sqrt(fact(i) + i ** 3))
	return sum + recursion(i + 1, n, x, sum)

x = int(input("Введите число x: "))
i = int(input("Введите число i: "))
n = int(input("Введите число n: "))
print(recursion(i, n, x, 0))