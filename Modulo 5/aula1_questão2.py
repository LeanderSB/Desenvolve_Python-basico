import random
import math

n = int(input("Digite a quantidade de números a serem gerados: "))
numeros = [random.randint(0, 100) for _ in range(n)]
soma = sum(numeros)
raiz_quadrada = math.sqrt(soma)
print(f"Os números gerados foram: {numeros}")
print(f"A soma dos números é: {soma}")
print(f"A raiz quadrada da soma é: {round(raiz_quadrada, 2)}")
