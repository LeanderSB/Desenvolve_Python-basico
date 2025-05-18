#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. 
# Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.

numero = input("Digite o número: ")

if len(numero) == 8:
    numero = "9" + numero

if len(numero) == 9 and numero[0] == "9":
    print("Número completo:", numero[:5] + "-" + numero[5:])
else:
    print("Número inválido.")
