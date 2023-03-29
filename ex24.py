# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

print(""" 
================ MENU ================
[+] Addition
[-] Subtraction
[*] Multiplication
[/] Division
======================================
""")

numb1 = float(input("Choose the 1º number: "))
numb2 = float(input("Choose the 2º number: "))

choice = str(input("Choose an operation: "))

if choice == "+": 
    result = numb1 + numb2
elif choice == "-":
    result = numb1 - numb2
elif choice == "*":
    result = numb1 * numb2
elif choice == "/":
    result = numb1 / numb2
else:
    print("Invalid data...")



if result % 2 == 0:
    result1 = "even"
else:
    result1 = "odd"

if result >= 0:
    result2 = "positive"
else:
    result2 = "negative"

if result % 1 == 0: 
    result3 = "integer"
else:
    result3 = "decimal"


print(f"The result is {result:.2}, an {result1}, {result2}, {result3} number!")