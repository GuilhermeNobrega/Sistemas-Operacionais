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
