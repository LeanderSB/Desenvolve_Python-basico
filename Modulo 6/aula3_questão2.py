import random

# ===================== Exercício 2 =====================
# Extração de domínios de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = [url[4:-4] for url in urls]  # Remove "www." e ".com" usando fatiamento

print("\nURLs:", urls)
print("Domínios extraídos:", dominios)