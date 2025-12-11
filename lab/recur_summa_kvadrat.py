#сумма увардарат 

def Q(n, k=1):
    if n == 1:
        return k
    return Q(n - 1 ** 2, k + n ** 2)

print(Q(2))
    
    