while True:
    try:
        n = int(input("Кол-во дней: "))
        if n <= 0:
            print("Ошибка: количество дней должно быть больше нуля!")
            continue
        break
    except ValueError:
        print("Ошибка: введите целое число!")

hours = n * 24
minutes = hours * 60

print(f"Часов: {hours}")
print(f"Минут: {minutes}")
