import random

def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
        estagios = f.read().split("\n\n")
        print(estagios[min(erros, len(estagios)-1)])

with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = f.read().splitlines()

palavra = random.choice(palavras).lower()
descoberta = ["_" for _ in palavra]
tentativas = []
erros = 0

while erros < 6 and "_" in descoberta:
    print("\nPalavra:", " ".join(descoberta))
    letra = input("Digite uma letra: ").lower()

    if letra in tentativas:
        print("Você já tentou essa letra.")
        continue

    tentativas.append(letra)

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                descoberta[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

if "_" not in descoberta:
    print(f"\nParabéns! Você acertou a palavra: {palavra}")
else:
    print(f"\nVocê perdeu! A palavra era: {palavra}")
