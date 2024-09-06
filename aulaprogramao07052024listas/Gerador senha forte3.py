import random

# Definir os conjuntos de caracteres
digitos = '1234567890'
maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculo = 'abcdefghijklmnopqrstuvwxyz'
especiais = '!@#$%&*()'

# Perguntar ao usuário sobre o comprimento total da senha
tamanho_senha = int(input("Digite o comprimento total da senha: "))

# Perguntar ao usuário sobre o número de caracteres de cada tipo
tamanho_maiusculo = int(input("Digite o número de caracteres maiúsculos na senha: "))
tamanho_minusculo = int(input("Digite o número de caracteres minúsculos na senha: "))
tamanho_digitos = int(input("Digite o número de caracteres numéricos na senha: "))
tamanho_especiais = int(input("Digite o número de caracteres especiais na senha: "))

# Verificar se a soma dos tamanhos dos caracteres não excede o comprimento total da senha
if tamanho_maiusculo + tamanho_minusculo + tamanho_digitos + tamanho_especiais > tamanho_senha:
    print("A soma dos tamanhos dos caracteres excede o comprimento total da senha. Por favor, tente novamente.")
else:
    # Inicializar a lista de caracteres da senha
    senha = []

    # Adicionar caracteres aleatórios de cada conjunto à senha
    senha.extend(random.choices(maiusculo, k=tamanho_maiusculo))
    senha.extend(random.choices(minusculo, k=tamanho_minusculo))
    senha.extend(random.choices(digitos, k=tamanho_digitos))
    senha.extend(random.choices(especiais, k=tamanho_especiais))

    # Calcular o número de caracteres restantes para completar a senha
    tamanho_restante = tamanho_senha - (tamanho_maiusculo + tamanho_minusculo + tamanho_digitos + tamanho_especiais)

    # Adicionar caracteres aleatórios do conjunto de caracteres restantes à senha
    senha.extend(random.choices(digitos + maiusculo + minusculo + especiais, k=tamanho_restante))

    # Misturar os caracteres da senha
    random.shuffle(senha)

    # Juntar os caracteres em uma string e exibir a senha
    senha_str = ''.join(senha)
    print("Sua senha gerada é:", senha_str)
