while True:
    user_input = input("Введите целое десятичное число: ").strip()
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        break
    print("Ошибка ввода!")

print(f"Двоичная: {bin(number)[2:]}")
print(f"Восьмеричная: {oct(number)[2:]}")
print(f"Шестнадцатеричная: {hex(number).upper()[2:]}")
