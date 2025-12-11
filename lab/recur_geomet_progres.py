#сумма геометрической прогресии 

def G(a, r, n, k=0):
    if n == 1:
        return a
    return a + r * G(n - 1, a, r)

print(G(2, 2, 3))