s = int(input("n:"))
roman_dict = {
        "I":1, 
        "V":5,
        "X":10, 
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
prev_value = 0
total = 0
for letter in reversed(s):
    value = roman_dict.get(letter) 
    if value > prev_value:
        total -= value
    else:
        total += value 
    prev_value = value
    print(total)





