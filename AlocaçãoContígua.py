'''Desenvolva em qualquer linguagem que interprete a alocação contígua:

First-fit → primeiro bloco disponível
Best-fit → o bloco que deixa menos espaço livre
Worst-fit → o maior bloco de espaço livre'''

#--> !pip install colorama
from colorama import Fore, Style

cores = [Fore.RED, Fore.GREEN, Fore.BLUE]

itens = ["[x]", "[y]", "[z]"]

for cor, item in zip(cores, itens):
    texto_formatado = f"{cor}{item}{Style.RESET_ALL}"
    print(texto_formatado)

from colorama import Fore, Style

cores = [Fore.RED, Fore.GREEN, Fore.BLUE]
itens = []
#itens = ["[x]", "[y]", "[z]"]
x = input("Digite nome do processo 1:")
itens.append(x)
y = input("Digite nome do processo 2:")
itens.append(y)
z = input("Digite nome do processo 3:")
itens.append(z)
for cor, item in zip(cores, itens):
    texto_formatado = f"{cor}{item}{Style.RESET_ALL}"
    print(texto_formatado)



#---------------------------------------------- one ------------------------------------------
from colorama import Fore, Style
from random import randint, choice

lista_nomes = ['ay1', 'bu3', 'g8s', 'j84', 'e3a', 'p9p', '8cz', 'b4f', '1q1', 'w3w', '5ff', '6fh', 'c6c', '0o0', '9iu', '9n0', 'a4f', 'b87', 'a77',
              '8z2', '1z3', '4z5', 'cv5', 'cv1', 'z9l', 'z0ç', 'Z3D', 'fk4', 'mt9', 'ar4', 'fm1', 'ct3', 'r31']

cores = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.BLACK, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.GREEN, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX]
itens = []
for i in range(1, 11):
    randoms = randint(50, 200)
    names = choice(lista_nomes)
    processo_cor = cores[i - 1]
    item = {
        f"{processo_cor}BLOCO MEMÓRIA [{i}]": f"VALOR_MEMORIA: {randoms}MB/s{Style.RESET_ALL}",
        "PROCESSO": f"-> {names}"
    }
    itens.append(item)

for item in itens:
    for key, value in item.items():
        print(f"{key}: {value}")

while True:
    NOME_PROCESSO = str(input("NOME SEU PROCESSO: "))
    VALOR_PROCESSO = int(input("VALOR DO PROCESSO: "))
    escolha = int(input("""Qual você deseja escolher?
    [1] - BestFit
    [2] - WorstFit
    [3] - FirstFit
    [0] - Exit\n"""))

    if escolha == 3:
        itens[0]["BLOCO MEMÓRIA [1]"] = f"VALOR_MEMORIA: {VALOR_PROCESSO}MB/s"
        itens[0]["PROCESSO"] = f"-> {NOME_PROCESSO}"

        for key in list(itens[0].keys()):
            if key != "BLOCO MEMÓRIA [1]" and key != "PROCESSO":
                del itens[0][key]

        for item in itens:
            for key, value in item.items():
                print(f"{key}: {value}")

    elif escolha == 0:
        break
