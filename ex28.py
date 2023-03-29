# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# Double Fillet      4,90U$ per Kg          5,80U$ per Kg
# Rib Eye Steak      5,90U$ per Kg          6,80U$ per Kg
# Rump Cap           6,90U$ per Kg          7,80U$ per Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("+=+=+=+=+=+=+=+=+=+=+=+= Hypermarket Tabajara +=+=+=+=+=+=+=+=+=+=+=+=")
print(""" 
                       Up to 5 Kg             Above 5 Kg
[1] Double Fillet      4,90U$ per Kg          5,80U$ per Kg
[2] Rib Eye Steak      5,90U$ per Kg          6,80U$ per Kg
[3] Rump Cap           6,90U$ per Kg          7,80U$ per Kg
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
""")

choise= int(input("Which do you want? "))
kg = float(input("How many kg do you want? "))
card = str(input("Do you have our Tabajara card? [Y]/[N]"))

price = 0 
discount = 0


if choise == 1:
    meat = "Double Fillet"
    if kg <= 5:
        price = kg * 4.5
    else:
        price = kg * 5.8

if choise == 2:
    meat = "Rib Eye Steak"
    if kg <= 5:
        price = kg * 5.9
    else: 
        price = kg * 6.8

if choise == 3:
    meat = "Rump Cap"
    if kg <= 5:
        price = kg * 6.9
    else:
        price = kg * 7.8


if card == "Y" or card == "y":
    discount = price - (price * 0.05)
    print(f"Type of meat: {meat}\nKG: {kg}\nTotal Price: {price:.2f}U$\nForm of payment: Card\nDiscount: 5%\nFinal Price: {discount:.2f}U$ ")

elif card == "N" or card == "n":
    print(f"Type of meat: {meat}\nKG: {kg}\nForm of payment: Money\nFinal Price: {price:.2f}U$ ")


