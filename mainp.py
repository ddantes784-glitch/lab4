while True:
    try:
        weight = float(input("Введите вес в кг: "))
        height = float(input("Введите рост в метрах (например, 1.75): "))
        if weight > 0 and height > 0:
            break
        print("Значения должны быть больше нуля!")
    except ValueError:
        print("Ошибка! Введите числа.")

imt = weight / (height ** 2)
print(f"\nВаш ИМТ: {imt:.2f}")

if imt < 18.5:
    print("Категория: Недостаточный вес")
elif imt < 25:
    print("Категория: Норма")
elif imt < 30:
    print("Категория: Избыточный вес")
else:
    print("Категория: Ожирение")
