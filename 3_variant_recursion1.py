import math
def recursion(k, x):
	if k == 1:
		return 1
	else:
		return (1 + math.sin(k * x) / k * (k - 1)) * recursion(k - 1, x)

n = int(input("Введите число n: "))
x = int(input("Введите число x: "))
print(recursion(n, x))

