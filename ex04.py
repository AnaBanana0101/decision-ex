# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letter = str(input("Choose a letter: "))

vowels = "aeiou"

if letter in vowels or letter in vowels.upper(): 
    print("The letter chosen is a vowel")
else:
    print("The letter chosen is a consonant")
