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

summ = a + b

if a > b:
    print(f"{a} больше, чем {b}")
elif a < b:
    print(f"{b} больше, чем {a}")
else:
    print(f"{a} и {b} равны")

print(f"Сумма чисел a и b = {summ}")
