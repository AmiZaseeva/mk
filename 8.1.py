def CircleS(R):
    S=3.14*R**2
    return S
try:
    R1=float(input("Введите радиус первого круга:"))
    R2=float(input("Введите радиус второго круга:"))
    R3=float(input("Введите радиус третьего круга:"))
except ValueError:
    print("Ошибка ввода данных")
else:
    S1=CircleS(R1)
    S2=CircleS(R2)
    S3=CircleS(R3)
print("Площадь первого круга:",S1)
print("Площадь второго круга:",S2)
print("Площадь третьего круга:",S3)
