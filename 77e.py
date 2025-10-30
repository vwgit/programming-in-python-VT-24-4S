x = int(input("Введите число x: "))
result = 0
deg = 1
fact = 1
step = False
plus = True
for i in range(1, 13):
    if i % 2 == 0:
        step = not step

    if step:
        continue

    deg = deg * x
    fact = fact * i
    if plus:
        result = result + deg / fact
    else:
        result = result - deg / fact
    plus = not plus
print("Результат:", result)