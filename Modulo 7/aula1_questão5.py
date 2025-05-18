#Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. 
# Dica: letra in "aeiou".

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
indices = [i for i, letra in enumerate(frase) if letra in vogais]

print(len(indices), "vogais")
print("Índices", indices)
