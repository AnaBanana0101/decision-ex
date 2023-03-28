# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 

hours = int(input("Enter the total hours worked in the month:\n"))
value_hour = float(input("Enter how much you earn per hour worked:\n"))


wage = value_hour * hours
inss = wage * 0.1
syndicate = wage * 0.03
fgts = wage * 0.11
total_discounts = inss + syndicate + fgts


if wage <= 900: 
    net_wage = wage - syndicate - inss
    print(f"Gross wage: U${wage}\nIR (0%) - NONE\nINSS (10%) - U${inss}\nFGTS - U${fgts}\nSyndicate (3%) - U${syndicate}\nTotal discounts - U${total_discounts}\nNet wage - U${net_wage}")

elif 901 < wage <= 1500: 
    ir = wage * 0.05 
    net_wage = wage - ir - syndicate - inss
    print(f"Gross wage: U${wage}\nIR (5%) - U${ir}\nINSS (10%) - U${inss}\nFGTS - U${fgts}\nSyndicate (3%) - U${syndicate}\nTotal discounts - U${total_discounts}\nNet wage - U${net_wage}")

elif 1501 < wage <= 2500: 
    ir = wage * 0.1 
    net_wage = wage - ir - syndicate - inss
    print(f"Gross wage: U${wage}\nIR (10%) - U${ir}\nINSS (10%) - U${inss}\nFGTS - U${fgts}\nSyndicate (3%) - U${syndicate}\nTotal discounts - U${total_discounts}\nNet wage - U${net_wage}")

else:
    ir = wage * 0.2 
    net_wage = wage - ir - syndicate - inss
    print(f"Gross wage: U${wage}\nIR (20%) - U${ir}\nINSS (10%) - U${inss}\nFGTS - U${fgts}\nSyndicate (3%) - U${syndicate}\nTotal discounts - U${total_discounts}\nNet wage - U${net_wage}")
