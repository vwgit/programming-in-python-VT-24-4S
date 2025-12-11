import math
def sum_of_squares_unique(n, seen = None):

	if seen is None:
		seen = set()

	if n == 0:
		return 0

	digit = n % 10
	rest = n // 10

	if digit not in seen:
		seen.add(digit)
		return digit * digit + (sum_of_squares_unique(rest, seen))
	else:
		return sum_of_squares_unique(rest, seen)

n = 22345
print(f"Результат: {sum_of_squares_unique(n)}")