def collect_keys(n):
	def pulling_keys(values, keys, index):
		if index == len(keys):
			return []
		key = keys[index]
		res = [key]
		value = values[key] 
		if isinstance(value, dict):
			res = res + pulling_keys(value,list(value.keys()), 0)
		return res + pulling_keys(values, keys, index+1)
	return pulling_keys(n, list(n.keys()), 0)

my_Set = {"a" : 1,"b" : {"c" : 2, "d" : 3, "e" : 4, "f" : 5}}

print("Полученный список: ", collect_keys(my_Set))