# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

year = int(input("Choose a year: "))

if (year % 4 == 0 and year % 100!=0) or (year % 400 == 0):
    print("The year is a leap year!")
else: 
    print("THe year is not a leap year...")