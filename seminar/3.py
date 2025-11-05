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

arif = (a + b + c) // 3
print(f"Среднее арифметическое трёх чисел: {arif}")