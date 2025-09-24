# факториал
n = int(input("Ведите число n: "))
result = 1

for i in range(2, n + 1):
    result = result * i
    print(result)