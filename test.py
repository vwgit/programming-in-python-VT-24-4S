def user_power(n, pow):
	if pow < 1:
		return 1
	total = 1
	total = total * n
	return total * user_power(n, pow - 1)

print("2^3 = " + str(user_power(2, 8)))