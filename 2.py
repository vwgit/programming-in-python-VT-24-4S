def S(n, k, sum):
    if n == 1:
        return 1
    elif k < n - 1:
        return S(n, k + 1, sum + n)
    else:
        return sum

print(S(5, 1, 0))