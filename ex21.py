# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

money = int(input("How much do you wanna withdraw: "))


if  10 <= money <= 600: 

    hundreds = money // 100
    money = money - (hundreds * 100)

    fiftys = money // 50
    money = money - (fiftys * 50)

    tens = money // 10
    money = money - (tens * 10)

    fives = money // 5
    money = money - (fives * 5)

    ones = money

    print(f""" 
    100 U$ banknotes: {hundreds}
    50U$ banknotes: {fiftys}
    10U$ banknotes: {tens}
    5U$ banknotes: {fives}
    1U$ banknotes: {ones}
""")

else:
    print("Invalid amount...")