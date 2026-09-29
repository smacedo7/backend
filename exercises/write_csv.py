import csv

i = ' '

with open("alunos.csv", "w", newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)

    while i not in "n":
        print("insira o nome do aluno")
        nome = input().strip().lower()
        print("insira a nota do aluno")
        nota = float(input())

        escritor.writerow([nome, nota])

        i = str(input("voce deseja continuar? [s][n]")).strip().lower()
        if i[0] == "n":
            break

with open("alunos.csv", "r", newline='', encoding='utf-8') as f:
    leitor = csv.reader(f)

    for linha in leitor:
        nome = linha[0]
        nota = linha[1]

        if float(nota) >= 7:
            print(nome, nota)
