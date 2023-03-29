# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("We ONLY accept Yes or No for answer!")
question1 = str(input("Did you call the victim? "))
question2 = str(input("Where you at the crime scene? "))
question3 = str(input("Owed to the victim? "))
question4 = str(input("Have you ever worked with the victim? "))
question5 = str(input("Do you live near the victim? "))

suspicion = 0

if question1 == "Yes": 
    suspicion += 1 
elif question1 == "No":
    suspicion += 0
else: 
    print("Answer correctly the question please...")
    

if question2 == "Yes": 
    suspicion += 1 
elif question2 == "No":
    suspicion += 0
else: 
    print("Answer correctly the question please...")

if question3 == "Yes": 
    suspicion += 1 
elif question3 == "No":
    suspicion += 0
else: 
    print("Answer correctly the question please...")

if question4 == "Yes": 
    suspicion += 1 
elif question4 == "No":
    suspicion += 0
else: 
    print("Answer correctly the question please...")

if question4 == "Yes": 
    suspicion += 1 
elif question4 == "No":
    suspicion += 0
else: 
    print("Answer correctly the question please...")

if suspicion == 0:
    print("You qualify as an inocent.")
elif suspicion == 2:
    print("You qualify as a suspect.")
elif suspicion == 3 or suspicion == 4:
    print("You qualify as an accomplice.")
else:
    print("You qualify as an assassin!")



