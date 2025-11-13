def nested_dict(n):
	if n == 1:
		return "{'level' : 1, 'next': None}"
	return "{'level' " + str(n) + ": , 'next': " + nested_dict(n - 1) + "}"

print(nested_dict(3))

