count = 0
total = 0
45
number = int(input('Введите числа: '))

if number == 0:
    print("первое число не можеть быть ноль")

else:
    while number != 0:
        total += number
        count += 1
        number = int(input("Вводите числа, для отсановки введите ноль: "))

average = total / count 
print(f"Среднее {average}")
