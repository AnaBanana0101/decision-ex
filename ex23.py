# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

number = float(input("Choose a number: "))

if number % 1 == 0: 
    print("The number that you chose is integer.")

else:
    print("The number that you chose is decimal.")