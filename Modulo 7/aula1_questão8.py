#Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima 
# "Válido" ou "Inválido". 

#O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF 
# (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes 
# a partir do número 2.

def calcular_digito(cpf, multiplicadores):
    soma = sum(int(d) * m for d, m in zip(cpf, multiplicadores))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

cpf_input = input("Digite o CPF (XXX.XXX.XXX-XX): ").replace(".", "").replace("-", "")

if len(cpf_input) != 11 or not cpf_input.isdigit():
    print("CPF inválido (formato incorreto).")
else:
    nove_digitos = cpf_input[:9]
    digito1 = calcular_digito(nove_digitos, range(10, 1, -1))
    digito2 = calcular_digito(nove_digitos + digito1, range(11, 1, -1))
    
    if cpf_input[-2:] == digito1 + digito2:
        print("Válido")
    else:
        print("Inválido")
