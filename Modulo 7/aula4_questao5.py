livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    # Adicione mais 8 livros aqui
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        f.write(",".join(map(str, livro)) + "\n")
