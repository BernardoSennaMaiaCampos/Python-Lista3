numeros=[1,2,6,8,'bob','pedro', 'felipe', 2.1, 'Bernardo']
num1 = numeros[0:4] and numeros[8]
s1=numeros[4:7]
print(numeros)
print(numeros[2])
print(numeros[1:3])

print(num1)
print(s1)

tamanho=len(numeros)
print(f'a lista tem {tamanho} elementos')

#########################################################

numeros=[1,2,6,8,'bob','pedro', 'felipe', 2.1, 'Bernardo']

novoItem=str(input('entre com um novo elemento: '))
numeros.append(novoItem)

print(numeros)