while True:
    a = input("Введите одну букву: ").lower()

    if len(a) != 1:
        print("Ошибка: введите только одну букву!")
        continue

    if not a.isalpha():
        print("Ошибка: введите именно букву, а не цифру или символ!")
        continue

    break

mas_a = ["a", "e", "i", "o", "u"]

if a in mas_a:
    print("Это гласная буква")
elif a == "y":
    print("Эта буква может быть гласной")
else:
    print("Это согласная буква")
