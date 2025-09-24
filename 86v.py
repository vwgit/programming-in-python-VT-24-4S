n = int(input("Введите число n: "))
sum = 0
while n > 0:
    number = n % 10
    n = n // 10
    sum = sum + number
print(sum)