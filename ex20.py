# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10

grade1 = float(input("1º grade: "))
grade2 = float(input("2º grade: "))
grade3 = float(input("3º grade: "))

avarage_grade = (grade1 + grade2 + grade3) / 3 

if avarage_grade >= 7:
    situation = "APPROVED"

elif avarage_grade == 10: 
    situation = "APPROVED WITH DISTINCTION"

else:
    situation = "DISAPPROVED" 

print(f"Your final avarage grade is {avarage_grade:.1f} and you're {situation}.")