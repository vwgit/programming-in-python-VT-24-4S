a = input("Введите число a: ")
mas_a = ["a", "e", "i", "o"]
for j in mas_a:
    if a == "y" or a == "u":
        print("это буква может быть гласной")
    elif a == mas_a[j]:
        print("это гласная буква")
    else:
        print("это согласная буква")

