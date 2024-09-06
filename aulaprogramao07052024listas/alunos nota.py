numeroAlunos = 2
numNotas = 4
notas =[]
alunos = []
for i in range(numeroAlunos):
    alunos.append(input(f'Digite o nome do {i+1} aluno: '))
    notasAluno = []
    for j in range(numNotas):
        notasAluno.append(float(input(f'Digite a {j+1} nota: ')))

    notas.append(notasAluno)
print(notas)
for i in range(numeroAlunos):
    print(f"\n As notas do aluno {alunos[i]} são {notas[i]}")
    print(f"A maior nota é {max(notas[i])} e a menor é {min(notas[i])}")
    print(f'A média das notas é {sum(notas[i])}/numNotas: .2f.\n')