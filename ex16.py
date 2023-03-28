# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

a = int(input("Enter the 1º number: "))

if a == 0:
    print("Invalide Value...")
else:
    b = int(input("Enter the 2º number: "))
    c = int(input("Enter the 3º number: "))
    delta = (b**2) - (4 * a * c)
        
    if delta < 0: 
        print("The delta result is a negative number, so there are no real roots.")
    elif delta == 0:
        root = -b / (2 * a)
        print(f"Delta is iqual 0, therefore it has just one real root: {root}")
    else:       
        x1 = (-b + delta**(1/2)) / (2 * a)
        x2 = (-b - delta**(1/2)) / (2 * a)
        print(f"Theres 2 real roots, x1 {x1} and {x2}")

