import random


digitos = '1234567890'
maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculo = 'abcdefghijklmnopqrstuvwxyz'
especiais = '!@#$%&*()'

def main():

    usaMaiusculo = input("Deseja incluir caracteres maiúsculos na senha? (S/N): ").upper()
    usaMinusculo = input("Deseja incluir caracteres minúsculos na senha? (S/N): ").upper()
    usaDigitos = input("Deseja incluir caracteres numéricos na senha? (S/N): ").upper()
    usaEspeciais = input("Deseja incluir caracteres especiais na senha? (S/N): ").upper()

    def opcao():

        opcoes = ''
        if usaMaiusculo == 'S':
            opcoes += maiusculo
        if usaMinusculo == 'S':
            opcoes += minusculo
        if usaDigitos == 'S':
            opcoes += digitos
        if usaEspeciais == 'S':
            opcoes += especiais
        if usaMaiusculo != 'S' or 'N' | usaMinusculo != 'S'or 'N' | usaDigitos != 'S' or 'N' | usaEspeciais != 'S' or 'N':
            print("Opção inválida, por favor, tente novamente.")
            main()
        
        if not opcoes:
            print("Você deve selecionar pelo menos uma opção de caracteres para a senha, por favor, tente novamente.")
            main()
        else:
            
            tamanhoSenha = int(input("Digite o comprimento total da senha: "))
            if tamanhoSenha <= 3:
                print("Comprimento inválido. Para que a senha seja gerada, é necessário que se tenha um comprimento mínimo de 4 valores. Por favor, tente novamente.")
                opcao()
            
            else:
                senha = ''.join(random.choices(opcoes, k=tamanhoSenha))
           
            print("Sua senha gerada é:", senha)
            continua()
            
    def continua():
        continuar = input("Deseja gerar mais senhas? (S/N): ").upper()
        match continuar:
            case 'S':
                print("Você escolheu continuar.")
                main()
            case 'N':
                print("Você escolheu não continuar, gerador encerrado.")
                exit()
            case _:
                print("Opção inválida, favor tentar novamente.")
                continua()
    
    opcao()
main()

