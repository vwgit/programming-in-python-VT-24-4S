# сумма числа
n = int(input("Введите кол-во корней n:"))

sum_ = 0
while n > 0:
    mod = n % 10
    n = n // 10
    sum_ = sum_ + mod
print(sum_)