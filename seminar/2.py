a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
summ = a + b
if a > b:
    print(f"{a} больше чем {b}")
elif a < b:
    print(f"{b} больше чем {a}")
else:
    print(a, b, "раавны")
print(f"сумма чисел a и b = {summ}")

