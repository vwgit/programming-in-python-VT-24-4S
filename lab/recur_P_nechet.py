# проивзедение нечетных чисел

def P(n, k=1):
    if n == 1:
        return 1
    return P(n - 1) * (2 * n - 1)

print(P(4))