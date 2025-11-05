while True:
    try:
        n = float(input("Введи скорость в км/ч: "))
        if n < 0:
            print("Ошибка: скорость не может быть отрицательной!")
            continue
        break
    except ValueError:
        print("Ошибка: введите число!")

v_ms = n / 3.6
print(f"Скорость в м/с: {v_ms}")
