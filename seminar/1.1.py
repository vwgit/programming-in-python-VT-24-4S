while True:
    try:
        a = int(input("Введите число n: "))
        break
    except ValueError:
        print("Ошибка: введите целое число!")

if a % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")
