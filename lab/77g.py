import math
n = int(input("Введите число n: "))
sum_sin = 0
result = 0


for i in range(1, n + 1):
    sum_sin = sum_sin + math.sin(i)

    result = result + 1 / sum_sin
    print(f"Шаг {i}: {result}")

