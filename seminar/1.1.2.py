
ceny = [4.95, 9.95, 14.95, 19.95, 24.95]

print("Товары со скидкой 60%:")

for i in range(len(ceny)):
    staraya_cena = ceny[i]
    
    skidak = skidka = staraya_cena * 0.60
    
    novaya_cena = staraya_cena - skidka
    
    print(f"Товар {i+1}:")
    print(f"Было: ${staraya_cena}")
    print(f"Скидка: ${skidka}")
    print(f"Стало: ${novaya_cena}")
    print()