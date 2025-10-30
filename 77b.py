n = int(input("Введите число n: "))
result = 1
for i in range(1, n + 1):
    result = result * i
print(f"{n} равен {result}")