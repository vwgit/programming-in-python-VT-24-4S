#def power(x, n):
#	if n == 0:
#		return 1
#	return x * power(x, n - 1)
#
#print("2^3 = " + str(power(2, 3)))

def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n - 1)

print(f"Результат факториал 5 = {fact(5)})")