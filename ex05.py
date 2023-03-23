# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

tasting_n1 = float(input("Tasting note nº 1: "))
tasting_n2 = float(input("Tasting note nº 2: "))


average = (tasting_n1 + tasting_n2) / 2 
print(f"Your average this semester is {average}")


if average >= 7: 
    print("You passed!")
elif average == 10: 
    print("You wever approved with Distinction!")
else:
    print("You failed...")
