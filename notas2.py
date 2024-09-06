# Definição dos dados
respostas = [
    ["BOB",      "B", "E", "B", "E", "D", "B", "A", "A", "A", "E"],
    ["RODRIGO",  "B", "E", "D", "A", "D", "A", "C", "A", "B", "D"],
    ["PEDRO",    "B", "C", "D", "C", "D", "A", "C", "A", "C", "E"],
    ["GABRIELA", "B", "C", "A", "C", "D", "A", "D", "A", "A", "B"],
    ["LAURA",    "B", "E", "B", "C", "B", "A", "C", "A", "A", "E"],
    ["CARLOS",   "B", "B", "D", "A", "D", "D", "C", "A", "C", "B"],
    ["FLAVIO",   "B", "C", "D", "C", "B", "A", "C", "B", "A", "E"],
    ["CLARA",    "A", "C", "E", "D", "D", "B", "A", "A", "A", "A"],
    ["EDUARDA",  "B", "C", "D", "C", "D", "A", "C", "A", "A", "E"],
    ["MARIA",    "B", "D", "A", "C", "B", "C", "C", "A", "A", "E"]
]

gabarito = ["B", "C", "D", "C", "D", "A", "C", "A", "A", "E"]

# Função para calcular a nota de um aluno
def calcular_nota(respostas_aluno, gabarito):
    return sum(1 for r, g in zip(respostas_aluno, gabarito) if r == g)

# Lista para armazenar os resultados
resultados = []

# Calcular as notas de cada aluno
for aluno in respostas:
    nome = aluno[0]
    respostas_aluno = aluno[1:]
    nota = calcular_nota(respostas_aluno, gabarito)
    resultados.append((nome, respostas_aluno, nota))

# Ordenar os resultados por nota decrescente
resultados.sort(key=lambda x: x[2], reverse=True)

# Imprimir os resultados no formato desejado
for i, (nome, matriz, nota) in enumerate(resultados):
    print(f"{i + 1}º colocado: {nome}")
    print(f"Matriz de acertos: {matriz}")
    print(f"Nota final: {nota}")
    print()  # Linha em branco para separar os resultados