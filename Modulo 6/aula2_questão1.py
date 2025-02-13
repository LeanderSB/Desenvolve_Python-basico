import random

# ===================== Exercício 1 =====================
# Gere 20 valores inteiros aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

print("Lista ordenada (sem modificar a lista original):", sorted(valores))
print("Lista original:", valores)
print("Índice do maior valor da lista:", valores.index(max(valores)))
print("Índice do menor valor da lista:", valores.index(min(valores)))