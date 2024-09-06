# import random

# lista1=[]

# for i in range(20):
#     lista1.append(random.randint(1,100))

# print(lista1)

#############################################

import random

listaEntrada=[]
grandeLista=[]

for j in range(3):
    listaEntrada=[]
    for i in range(5):
        listaEntrada.append(random.randint(1,100))
    grandeLista.append(listaEntrada)
print(grandeLista)

l1=grandeLista[0]
print(f'a lista {l1} tem como soma {sum(l1)} e a media {sum(l1)/len(l1)}')

print(f'Lista ordenada {sorted(l1)}, maior/menor elemento {max(l1)} e {min(l1)}')