#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes.
#Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada
#respondente. Ao final, imprima a média das idades.

somaidade = 0
quant = 0

while True:
    idade = int(input("Qual a idade? "))
    fim = input("Deseja continuar? (Sim/Não) ").lower()
    if fim == "não":
        break

    somaidade += idade
    quant += 1

if quant > 0:
    media = somaidade / quant
    print(f"A média das idades é: {media:.2f}")
else:
    print("Nenhuma idade foi inserida.")
