from math import sqrt
n = int(input("Введите число n: "))
result = 0
for i in range(1, n + 1):
    result = sqrt(result + 2)
print("Результат:", result)