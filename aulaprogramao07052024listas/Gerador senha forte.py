import random

digitos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']
minusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
especiais = ['!', '@', '#', '$', '%', '&', '*', '(',')']




# tamanho = int(input("Digite o tamanho da senha: "))
print("\n\nDigite o tamanho da senha abaixo de acordo com os caracteres: ")
usaMaiusculo = input('\nUtilizar maiúsculos (S/N): ').upper()
tamanhoMaiusculo = int(input("Digite o tamanho de caracteres maiúsculos: "))
usaMinusculo = input('\n\nUtilizar minúsculos (S/N): ').upper()
tamanhoMinusculo = int(input("Digite o tamanho de caracteres minúsculos: "))
usaDigitos = input('\n\nUtilizar digitos (S/N) :').upper()
tamanhoDigitos = int(input("Digite o tamanho de caracteres numéricos: "))
usaEspeciais = input('\n\nUtilizar caracteres especiais (S/N): ').upper()
tamanhoEspeciais = int(input("Digite o tamanho de caracteres especiais: "))

# tamanhoMaiusculo
# tamanhoMinusculo
# tamanhoDigitos
# tamanhoEspeciais
# total = tamanho


gerarDigito = random.choices(digitos, weights=None, cum_weights=None, k = tamanhoDigitos)#, k=total)
gerarMaiusculo = random.choices(maiusculo, weights=None, cum_weights=None, k = tamanhoMaiusculo)#, k=total)
gerarMinusculo = random.choices(minusculo, weights=None, cum_weights=None, k = tamanhoMinusculo)#, k=total)
gerarEspeciais = random.choices(especiais, weights=None, cum_weights=None, k = tamanhoEspeciais)#, k=total)

if usaMaiusculo == 'S' and usaMinusculo == 'S' and usaDigitos == 'S' and usaEspeciais == 'S':
    print(gerarMaiusculo+gerarMinusculo+gerarDigito+gerarEspeciais)
elif usaMaiusculo == 'S' and usaMinusculo == 'S' and usaDigitos == 'S' and usaEspeciais == 'N':
    print(gerarMaiusculo+gerarMinusculo+gerarDigito)
elif usaMaiusculo == 'S' and usaMinusculo == 'S' and usaDigitos == 'N' and usaEspeciais == 'N':
    print(gerarMaiusculo+gerarMinusculo)
elif usaMaiusculo == 'S' and usaMinusculo == 'N' and usaDigitos == 'N' and usaEspeciais == 'N':
    print(gerarMaiusculo)
elif usaMaiusculo == 'N' and usaMinusculo == 'N' and usaDigitos == 'N' and usaEspeciais == 'S':
    print(gerarEspeciais)
elif usaMaiusculo == 'N' and usaMinusculo == 'N' and usaDigitos == 'S' and usaEspeciais == 'S':
    print(gerarDigito+gerarEspeciais)
elif usaMaiusculo == 'N' and usaMinusculo == 'S' and usaDigitos == 'S' and usaEspeciais == 'S':
    print(gerarMinusculo+gerarDigito+gerarEspeciais)
elif usaMaiusculo == 'S' and usaMinusculo == 'N' and usaDigitos == 'N' and usaEspeciais == 'S':
    print(gerarMaiusculo+gerarEspeciais)
elif usaMaiusculo == 'N' and usaMinusculo == 'S' and usaDigitos == 'S' and usaEspeciais == 'N':
    print(gerarMinusculo+gerarDigito)
elif usaMaiusculo == 'S' and usaMinusculo == 'N' and usaDigitos == 'S' and usaEspeciais == 'N':
    print(gerarMaiusculo+gerarDigito)
elif usaMaiusculo == 'N' and usaMinusculo == 'S' and usaDigitos == 'N' and usaEspeciais == 'S':
    print(gerarMinusculo+gerarEspeciais)
else:
    print("opção incorreta, por favor, tentar novamente")
    