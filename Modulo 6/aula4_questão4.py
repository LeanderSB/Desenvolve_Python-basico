# ===================== Exercício 4 =====================

# Reescrevendo o código para construir a lista aprovados usando compreensão de listas
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]
print("Aprovados:", aprovados)