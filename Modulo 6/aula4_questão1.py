# ===================== Exercício 1 =====================

# Lista de todos os números pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]
print("Números pares entre 20 e 50:", pares)

# Lista dos quadrados dos valores de [1,2,3,4,5,6,7,8,9]
quadrados = [x ** 2 for x in range(1, 10)]
print("Quadrados dos números de 1 a 9:", quadrados)

# Lista de todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print("Números entre 1 e 100 divisíveis por 7:", divisiveis_por_7)

# Lista de "par" ou "ímpar" para valores em range(0, 30, 3)
paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print('Paridade para valores de range(0, 30, 3):', paridade)