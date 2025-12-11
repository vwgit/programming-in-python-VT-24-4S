#5вар 2 задание(рекурсия)
def collect_keys(d):
	def helper(dict_obj, keys_list, index):
	
		if index == len(keys_list):
			return []

		key = keys_list[index]
		value = dict_obj[key] 
		
		result = [key]
	
		if isinstance(value,dict):
			result += helper(value,list(value.keys()), 0)
		return result + helper(dict_obj, keys_list, index + 1)
	return helper(d, list(d.keys()), 0)
ex={"a" : 1,"b" : {"c" : 2, "d" : 3}}
print(collect_keys(ex))