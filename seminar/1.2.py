n = int(input("Введите возраст собаки: "))
if n <= 2:
    human_age = n * 10.5
    print(f"Возраст собавки в человеческих: {human_age}")
else:
    human_age = 2 * 10.5 + (n - 2) * 4
    print(f"Возраст собавки в человеческих: {human_age}")
