import random
# ===================== Exercício 4 =====================
# Receba duas listas de tamanhos diferentes do usuário e combine-as alternadamente
print("\n=== Combinação Alternada de Listas ===")
tamanho1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o elemento {i + 1} da lista 1: ")) for i in range(tamanho1)]

tamanho2 = int(input("\nDigite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o elemento {i + 1} da lista 2: ")) for i in range(tamanho2)]

# Combine as listas alternadamente
lista_intercalada = []
for i in range(max(len(lista1), len(lista2))):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])

print("\nLista intercalada:", lista_intercalada)