while True:
    try:
        a = int(input("Введите число a: "))
        break
    except ValueError:
        print("Ошибка: введите целое число!")

while True:
    try:
        b = int(input("Введите число b: "))
        break
    except ValueError:
        print("Ошибка: введите целое число!")

while True:
    try:
        c = int(input("Введите число c: "))
        break
    except ValueError:
        print("Ошибка: введите целое число!")

v = a * b * c
s = 2 * c * (a + b)

print(f"Объём: {v}")
print(f"Площадь поверхности: {s}")
