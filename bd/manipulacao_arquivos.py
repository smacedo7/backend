with open('dados.txt', 'w') as f:
    f.write("Hello, world!")

with open("dados.txt", 'r') as f:
    arquivo = f.read()

print(arquivo)


import csv

with open('dadox.csv', 'w') as f:
    escritor = csv.writer(f)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["samuel", 19])

with open("dadox.csv", newline='') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)

import json

dados = {
    'nome': 'Ana',
    'idade': 32,
    'enderecos': ['Endereço A', 'Endereço B']
}

with open("teste_json.json", 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

with open("teste_json.json", 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)
    print(dados_lidos)
