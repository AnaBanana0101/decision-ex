# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

grade1 = float(input("Enter the 1º grade: "))
grade2 = float(input("Enter the 2º grade: "))

grade_avarage = (grade1 + grade2) / 2

if grade_avarage >= 9 and grade_avarage <= 10: 
    concept = "A"
    situation = "Approved!"
elif 7.5 <= grade_avarage <= 8.9:
    concept = "B"
    situation = "Approved!"
elif 6 <= grade_avarage <= 7.4:
    concept = "C"
    situation = "Approved!"
elif 4 <= grade_avarage <=5.9:
    concept = "D"
    situation = "Reprobate.."
else:
    concept = "E"
    situation = "Reprobate.."

print(f"1º Grade: {grade1:.1f} - 2º Grade: {grade2:.1f}\nGrade Avarage: {grade_avarage:.1f}\nConcept - {concept}\n{situation}")