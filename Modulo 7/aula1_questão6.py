#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. 
# Anagramas são palavras com os mesmos caracteres rearranjados.

from itertools import permutations

frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

palavras = frase.split()
anagramas = []

for palavra in palavras:
    if sorted(palavra.lower()) == sorted(objetivo.lower()) and len(palavra) == len(objetivo):
        anagramas.append(palavra)

print("Anagramas:", anagramas)
