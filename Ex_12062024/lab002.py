a = int(input("Enter year:"))
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("this is a leap year")
else:
    print("this is not a leap year")
