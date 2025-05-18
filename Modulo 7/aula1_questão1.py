#Escreva um programa que solicita o nome do usuário e o imprime em forma de escada.

# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Imprime o nome em forma de escada
for i in range(1, len(nome) + 1):
    print(nome[:i])
