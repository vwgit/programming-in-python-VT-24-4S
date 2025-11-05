import math
def cossin(maximum, _cos, _sin, sum, count):
    if maximum < count:
        return sum
    else:
        new_sum = sum * (_cos / _sin)
        return cossin(new_sum * _cos / _sin, _sin + math.sin(count + 1), math.cos(count + 1), count + 1, maximum)

sum = 1
maximum = int(input("Введите число шагов: "))
count = 1
res = cossin(sum, math.sin(count), math.cos(count), count, maximum)
print(res)
