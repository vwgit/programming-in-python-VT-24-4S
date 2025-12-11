import math

def user_power(n, pow):
	if pow < 1:
		return 1
	total = 1
	total = total * n
	return total * user_power(n, pow - 1)

def calculating(n, x, y):
	if n < 1:
		return 1
	else:
		numerator = user_power(x, y)
		denumerator = math.sqrt(math.factorial(y) + math.factorial(x))
		current_term = numerator / denumerator
		return current_term * (current_term + calculating(n - 1, x, y))

n = 3
x = 3
y = 3
print(f"Результат: {calculating(n, x, y)}.")