a, b, operation = (
    float(input("Введите первое число: ")),
    float(input("Введите второе число: ")),
    input("Введите операцию (+, -, *, /): ").strip(),
)

match operation:
    case "+":
        print(f"Результат: {a + b}")
    case "-":
        print(f"Результат: {a - b}")
    case "*":
        print(f"Результат: {a * b}")
    case "/":
        if b == 0:
            print("Ошибка: делить на ноль нельзя!")
        else:
            print(f"Результат: {a / b:.2f}")
    case _:
        print("Неизвестная операция")
