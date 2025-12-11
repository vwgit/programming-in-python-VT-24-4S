#5вар 2 задание(рекурсия)
def collect_keys(d):
	keys = []
	def help(table):
		for key, value in table.items():
			keys.append(key)
			if isinstance(value,dict):
				help(value)
	help(d)
	return keys
print(collect_keys({"a" : 1,"b" : {"c" : 2, "d" : 3}}))