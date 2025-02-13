import random

# ===================== Exercício 2 =====================
# Gere um valor aleatório entre 5 e 20
num_elementos = random.randint(5, 20)
# Gere valores aleatórios entre 1 e 10 e armazene em uma lista
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print("\nLista elementos:", elementos)
print("Soma dos valores da lista:", sum(elementos))
print("Média dos valores da lista:", sum(elementos) / len(elementos))
