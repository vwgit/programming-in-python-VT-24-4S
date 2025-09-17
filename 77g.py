
from math import sin

n = int(input("Введите число n: "))
result = 0
sum = 0
for i in range(1, n):
    sum = sum + sin(i)
    result = result + 1/sum
print("Результат:", result)