side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))
if side1 == side2 and side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
