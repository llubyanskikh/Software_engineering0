a = int(input("Введите числовое значение от 0 до 10 включительно: a = "))
if a < 0 or a > 10:
    print(f"Значение6 {a} не соответствует условию. Введите числовое значение от 0 до 10 включительно:")
else:
    if a >= 0 and a <= 3:
        print("0<=a<=3")
    elif a >3 and a <= 6:
        print("3<a<=6")
    else:
        print("6<a<=10")