#Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova 
# frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da 
# palavra no lugar. 
import random

def embaralhar_palavras(frase):
    def embaralhar(palavra):
        if len(palavra) <= 3:
            return palavra
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]

    palavras = frase.split()
    return ' '.join(embaralhar(palavra) for palavra in palavras)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
