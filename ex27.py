# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


kg_strawberry = float(input("How many kilograms do you want of strawberries? "))
kg_apple = float(input("How many kilograms do you want of apples? "))

kg_total = kg_apple + kg_strawberry

price_strawberry = 0
price_apples = 0 
total_price = 0


if kg_apple >= 5 or kg_strawberry >= 5: 
    price_strawberry = kg_strawberry * 2.5
    price_apples = kg_apple * 1.8
    total_price = price_apples + price_strawberry

elif kg_apple <= 5 or kg_strawberry <= 5: 
    price_strawberry += kg_strawberry * 2.2
    price_apples = kg_apple * 1.5
    total_price = price_apples + price_strawberry


elif total_price < 25 or kg_total >= 8:
    total_price += total_price * 1 / 100

print(f"The amount to be paid is {total_price:.2f}U$. You ordered {kg_strawberry}kg of strawberry and {kg_apple}kg of apples, totalizing {kg_total}kg.")


