columnTitle = input("Введите название столбца: ")
alphabet = dict()
for i in range(65, 91):
    alphabet[chr(i)] = i - 64
result = 0
for letter in columnTitle.upper():
    result = result * 26 + alphabet[letter]
print(result)