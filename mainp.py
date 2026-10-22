try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))

    if x == 0 and y == 0:
        print("Точка находится в начале координат")
    elif x == 0:
        print("Точка находится на оси Y")
    elif y == 0:
        print("Точка находится на оси X")
    elif x > 0 and y > 0:
        print("1-я координатная четверть")
    elif x < 0 and y > 0:
        print("2-я координатная четверть")
    elif x < 0 and y < 0:
        print("3-я координатная четверть")
    else:
        print("4-я координатная четверть")
        
except ValueError:
    print("Ошибка! Введите числовые значения.")
