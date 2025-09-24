# произведение вида
n = int(input("Ведите число n: "))
result = 1

for i in range(2, n + 1):
    result = result * (1 + 1 / (i * i))
    print(result)