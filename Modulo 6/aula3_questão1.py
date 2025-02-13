import random

# ===================== Exercício 1 =====================
# Solicitar uma quantidade indefinida de números inteiros
numeros = []
while len(numeros) < 4:
    try:
        entrada = input("Digite um número inteiro (ou pressione Enter para terminar): ")
        if entrada == "":
            if len(numeros) >= 4:
                break
            else:
                print("Você deve inserir pelo menos 4 valores.")
        else:
            numeros.append(int(entrada))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("\nLista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
