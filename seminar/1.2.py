while True:
    try:
        n = float(input("Введите возраст собаки (в годах): "))
        if n <= 0:
            print("Ошибка: возраст должен быть положительным числом!")
            continue
        break
    except ValueError:
        print("Ошибка: введите число!")

if n <= 2:
    human_age = n * 10.5
else:
    human_age = 2 * 10.5 + (n - 2) * 4

print(f"Возраст собаки в человеческих годах: {human_age}")
