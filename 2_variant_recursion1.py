import math
def calculating(n, x, y):
	if n < 1:
		return 1
	else:
		numerator = x ** y
		denumerator = math.sqrt(math.factorial(y) + math.factorial(x))
		current_term = numerator / denumerator
		return current_term * (current_term + calculating(n - 1, x, y))

n = 3
x = 3
y = 3
print(f"Результат: {calculating(n, x, y)}.")


























total = 1
	
	str_number = str(number)
	if str_number[1] == str_number[0]:
		total = total + 