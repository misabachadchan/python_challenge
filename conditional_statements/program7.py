year=int(input("Enter year:"))
if (year%4==0 and year!=100) or year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not leap year")