# ===================== Exercício 2 =====================

# Solicitar uma frase do usuário
frase = input("\nDigite uma frase: ")

# Lista de vogais ordenada alfabeticamente
vogais = sorted([char for char in frase if char.lower() in 'aeiou'])
print("Vogais:", vogais)

# Lista de consoantes, sem espaços em branco
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']
print("Consoantes:", consoantes)
