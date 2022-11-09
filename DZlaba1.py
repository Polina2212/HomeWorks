a = float(input("Коэффициент a="))
b = float(input("Коэффициент b="))
c = float(input("Коэффициент c="))
D = (b**2-4*a*c)
if a == 0:
    print("Уравнение не является квадратным")
else:
    if D < 0:
        print("Уравнение не имеет корней")
    else:
        print(((-b+D**0.5)/(2*a)), ((-b-D**0.5)/(2*a)))