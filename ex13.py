#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

day = int(input("Chose a number os the 7 days week: "))

if day == 1:
    print("Sunday!")
elif day == 2:
    print("Monday!")
elif day == 3:
    print("Tuesday!")
elif day == 4:
    print("Wednesday!") 
elif day == 5:
    print("Thursday!")
elif day == 6:
    print("Friday!")
elif day == 7:
    print("Saturday!")  
else:
    print("Invalide number...")
