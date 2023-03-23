#Faça um Programa que leia três números e mostre-os em ordem decrescente.


# n1 = int(input("Choose the 1º number: "))
# n2 = int(input("Choose the 2º number: "))
# n3 = int(input("Choose the 2º number: "))

# numbers = [n1, n2, n3]
# numbers.sort(reverse = True)

# print(f"The ascending form of the chosen numbers {numbers}")


list = []
numbers = 3
for i in range(numbers):
    asc = int(input("Choose a number: "))
    list.append(asc)

list.sort(reverse = True)
print(list)