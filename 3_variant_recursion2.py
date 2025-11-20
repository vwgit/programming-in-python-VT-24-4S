def nested_dict(n):
	if n == 1:
		return {'level': 1, 'next': None}
	else:
		return {'level': n, 'next': nested_dict(n - 1)}

print(type(nested_dict(5)))