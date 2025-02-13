import random

# ===================== Exercício 3 =====================
# Preencha duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
# Intersecção sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

print("\nLista 1:", lista1)
print("Lista 2:", lista2)
print("Lista interseccao (ordenada):", interseccao)

# Contagem de elementos da interseção em cada lista
print("\nContagem:")
for elemento in interseccao:
    print(f"{elemento}: (lista1={lista1.count(elemento)}, lista2={lista2.count(elemento)})")