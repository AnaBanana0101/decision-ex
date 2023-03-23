# # Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

shift = str(input("In which shift do you study? [D] or [E] or [N]\n"))
shift.upper()

if shift == "d":
    print("Good day!")
elif shift == "e":
    print("Good evening!")
elif shift == "n":
    print("Good night!")
else:
    print("Invalide code...")
