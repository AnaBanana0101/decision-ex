# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sex = str(input("Which sex are you? [F] or [M] "))
sex = sex.upper()

if sex == "F":
    print("You are a female!")
elif sex == "M": 
    print("You are a male!")
else:
    print("Invalide...")