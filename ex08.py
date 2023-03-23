#Faça um programa que pergunte o preço de três produtos e informe qual 
#produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

price1 = float(input("Price of the 1º item: U$"))
price2 = float(input("Price of the 2º item: U$"))
price3 = float(input("Price of the 3º item: U$"))

if price1 < price2 and price1 < price3:
    print("Choose the 1º item, it's cheaper!")
elif price2 < price1 and price2 < price3:
    print("Choose the 2º item, it's cheaper!")
else:
    print("Choose the 3º item, it's cheaper!")