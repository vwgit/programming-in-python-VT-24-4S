#1вар 2 задание
def remove_digits(s):
	primes = {'2','3','5','7'}
	if s == "":
		return ""
	one = s[0]
	rest = s[1:]
	
	if one in primes:
		return remove_digits(rest)
	else:
		return one + remove_digits(rest)
print(remove_digits("abc123d4"))