#1 вар 1 задание
def fact(n):
	if n <=1:
		return 1
	return n*fact(n-1)
def S(n, x):
	if n==1:
		return x / (fact(1) + 1**2)
	return S(n-1, x) + x**n / (fact(n)+ n*n)
print(S(5,2)) 