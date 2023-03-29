# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: 
# A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


print("""======= Welcome to the gas station =======")
                [A] Alcohol
                [G] Gasoline
===========================================""")

liters = int(input("How many liters would you like to fill? "))
choice = str(input("Which one do you like to refuel with? "))
price = 0

if choice == "A":
    price = liters * 1.9
    if liters <= 20:
        price -= 1.9 * (liters * 0.03)
    else: 
        price -= 1.9 * (liters * 0.05)

elif choice == "G":
    price = liters * 2.5
    if liters <= 20: 
        price = 2.5 * (liters * 0.04)
    else:
        price = 2.5 * (liters * 0.06)
    
print(f"The amount to be paid is {price:.2f}U$.")
