#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês 
# por extenso. 
# Dica: usando listas você não precisa fazer um "if" para cada mês.
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split("/")

mes_extenso = meses[int(mes) - 1]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
