import random
# ===================== Exercício 3 =====================
# Lista de 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("\nLista original:", lista)

# Encontrar o intervalo com a maior quantidade de números negativos
max_negativos = 0
inicio_intervalo = 0
for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        intervalo = lista[i:j]
        num_negativos = sum(1 for x in intervalo if x < 0)
        if num_negativos > max_negativos:
            max_negativos = num_negativos
            inicio_intervalo = i
            fim_intervalo = j

# Deletar o intervalo com o maior número de negativos
del lista[inicio_intervalo:fim_intervalo]
print("Lista editada:", lista)