#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, 
# bem como a chave da criptografia. Regras:

#Chave de criptografia: gere um valor n aleatório entre 1 e 10

#Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis 
# (entre 33 e 126 na tabela Unicode)

import random

def encrypt(lista):
    chave = random.randint(1, 10)
    criptografados = []

    for nome in lista:
        criptografado = ''
        for c in nome:
            novo_codigo = ord(c) + chave
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            criptografado += chr(novo_codigo)
        criptografados.append(criptografado)

    return criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
criptografados, chave = encrypt(nomes)

print("Chave aleatória:", chave)
print("Nomes criptografados:", criptografados)
