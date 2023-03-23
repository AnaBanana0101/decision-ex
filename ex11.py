# #As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


salary = float(input("Insert your salary: "))


if salary <= 280: 
    rise = salary * 0.2
    increase = "20%"
    value = rise + salary

elif 281 < salary <= 699: 
    rise = salary * 0.15
    increase = "15%"
    value = rise + salary

elif 700 < salary <= 1499: 
    rise = salary * 0.1
    increase = "10%"
    value = rise + salary

else: 
    rise = salary * 0.05
    increase = "5%"
    value = rise + salary

print(f"Your current salary: R${salary:.2f}\nThe percentual rise: R${increase}\nIncreased value: R${rise:.2f}\nNew salary: R${value:.2f}")

