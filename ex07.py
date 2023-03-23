# Faça um Programa que leia três números e mostre o greater e o lesser deles

n1 = int(input("Choose the 1º number: "))
n2 = int(input("Choose the 2º number: "))
n3 = int(input("Choose the 3º number: "))


if n1 > n2 and n1 > n2: 
    greater = n1
elif n2 > n1 and n2 > n3:
    greater = n2
else:
    greater = n3

if n1 < n2 and n1 < n2: 
    lesser = n1 
elif n2 < n1 and n2 < n3:
    lesser = n2 
else:
    lesser = n3

print(f"The greater is {greater} and the lesser is {lesser}")