while True:
    try:
        sides = int(input("Введите количество сторон фигуры (3–10): "))
        if sides < 3:
            print("Ошибка: у многоугольника не может быть меньше 3 сторон!")
            continue
        break
    except ValueError:
        print("Ошибка: введите целое число!")

if sides == 3:
    print("Это треугольник")
elif sides == 4:
    print("Это четырёхугольник")
elif sides == 5:
    print("Это пятиугольник")
elif sides == 6:
    print("Это шестиугольник")
elif sides == 7:
    print("Это семиугольник")
elif sides == 8:
    print("Это восьмиугольник")
elif sides == 9:
    print("Это девятиугольник")
elif sides == 10:
    print("Это десятиугольник")
else:
    print("Фигуры с таким количеством сторон нет в диапазоне 3–10")
