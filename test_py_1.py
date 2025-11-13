def rec(n, k=1):
	if n == 1:
		return 1
	return 1 / (2 * k + 1) ** 2 + rec(n - 1)

print(rec(3))