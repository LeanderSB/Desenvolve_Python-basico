#Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. 
# Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.

# Solicita o nome
primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

# Concatena
nome_completo = primeiro_nome + " " + sobrenome

# Boas-vindas
print("Seja bem-vindo(a),", nome_completo + "!")
