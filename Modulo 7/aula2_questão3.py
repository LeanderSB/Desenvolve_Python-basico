#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo 
# (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, 
# e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que 
# o usuário digite "Fim".
import string

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break

    limpa = ''.join(c.lower() for c in frase if c.isalnum())

    if limpa == limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')

