#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

modificada = ''.join('*' if letra in vogais else letra for letra in frase)
print("Frase modificada:", modificada)
