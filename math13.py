s = input("Введите римское число: ")
s = s[::-1]
roman_numbers = {
    "I": 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000
}
sum = 0
prev_value = roman_numbers.get(s[0])
for letter in s:
    value = roman_numbers.get(letter)
    if prev_value > value:
        sum = sum - value
    else:
        sum = sum + value
    prev_value = roman_numbers.get(letter)
print(sum)