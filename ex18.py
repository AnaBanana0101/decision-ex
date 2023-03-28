# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

day = input("Choose a day: ")
month = input("Choose a month: ")
year = input("Choose a year: ")

validation = False

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): 
    day <= 31
    validation = True

elif (month == 4 or month == 6 or month == 9 or month == 11): 
    day <= 30
    validation = True

elif month == 2: 
    day <= 28
    validation = True
    if (year % 4 == 0 and year % 100!=0) or (year % 400 == 0):
        day <= 29
        validation = True

if(validation):
    print("The date is valide!")
else:
    print("Invalide date...")