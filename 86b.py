n = int(input("Введите число n: "))
count = 0
while n > 1:
    n = n / 10
    count = count + 1
print(count)