with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# As 25 primeiras linhas
print("PRIMEIRAS 25 LINHAS:")
print("".join(linhas[:25]))

# Número total de linhas
print(f"Número de linhas: {len(linhas)}")

# Linha com mais caracteres
maior_linha = max(linhas, key=len)
print("Linha com mais caracteres:")
print(maior_linha.strip())

# Contagem dos nomes
from collections import Counter

texto = "".join(linhas).lower()
contagem = Counter(re.findall(r'\bnonato\b|\bíria\b', texto))
print(f"Menções a Nonato: {contagem['nonato']}")
print(f"Menções a Íria: {contagem['íria']}")
