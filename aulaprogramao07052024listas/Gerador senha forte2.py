import random

# Definir os conjuntos de caracteres
digitos = '1234567890'
maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculo = 'abcdefghijklmnopqrstuvwxyz'
especiais = '!@#$%&*()'

# Inicializar a lista de caracteres da senha
senha = []

# Perguntar ao usuário sobre as opções da senha
tamanhoMaiusculo = int(input("Digite o número de caracteres maiúsculos na senha: "))
tamanhoMinusculo = int(input("Digite o número de caracteres minúsculos na senha: "))
tamanhoDigitos = int(input("Digite o número de caracteres numéricos na senha: "))
tamanhoEspeciais = int(input("Digite o número de caracteres especiais na senha: "))

# Adicionar caracteres aleatórios de cada conjunto à senha
senha.extend(random.choices(maiusculo, k=tamanhoMaiusculo))
senha.extend(random.choices(minusculo, k=tamanhoMinusculo))
senha.extend(random.choices(digitos, k=tamanhoDigitos))
senha.extend(random.choices(especiais, k=tamanhoEspeciais))

# Misturar os caracteres da senha
random.shuffle(senha)

# Juntar os caracteres em uma string e exibir a senha
senha_str = ''.join(senha)
print("Sua senha gerada é:", senha_str)
