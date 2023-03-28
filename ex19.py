# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de hundreds, dozens e unitys do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 hundreds, 2 dozens e 6 unitys
# 12 = 1 dozen e 2 unitys Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16



number = int(input("Choose a number: "))
unity = number % 10
dozen = (number % 100) // 10
hundred = number // 100
spacer1 = ""
spacer2 = ""

if hundred > 0 and dozen > 0 and unity > 0:
    spacer1 = " , "  
    spacer2 = " e "  

elif hundred > 0 and dozen > 0:
    spacer1 = " e "  
    spacer2 = ""

elif (hundred > 0 and unity > 0) or (dozen > 0 and unity > 0):
    spacer1 = "" 
    spacer2 = " e " 

if hundred > 0:
    if hundred == 1:
        hundred = "1 hundred"
    else:
        hundred = f"{hundred} hundreds"

else:
    hundred = ""
if dozen > 0:
    if dozen == 1:
        dozen = "1 dozen"
    else:
        dozen = f"{dozen} dozens"

else:
    dozen = ""

if unity > 0:
    if unity == 1:
        unity = "1 unity"
    else:
        unity = f"{unity} unitys"
        
else:
    unity = ""
    
print(f"{hundred}{spacer1}{dozen}{spacer2}{unity}")