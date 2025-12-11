#факториал

def Summa(n, k=1):
    if n == 1:
        return k
    return Summa(n - 1, k + n)

print(Summa(70))
    
    