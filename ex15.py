# # Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# # Dicas:
# # Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# # Triângulo Equilátero: três lados iguais;
# # Triângulo Isósceles: quaisquer dois lados iguais;
# # Triângulo Escaleno: três lados diferentes;

a = float(input("Enter the 1º side: "))
b = float(input("Enter the 2º side: "))
c = float(input("Enter the 3º side: "))



if (a + b < c) or (a + c < b) or (b + c < a):
    print("Entered data does not form a triangle.")
elif a == b == c: 
    print("The triangle formed is a equilateral triangle.")
elif a != b != c: 
    print("The triangle formed is a scalene triangle.")
else:
    print("The triangle formed is a isosceles triangle.")

