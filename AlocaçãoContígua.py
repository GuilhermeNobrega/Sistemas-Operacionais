'''Desenvolva em qualquer linguagem que interprete a alocação contígua:

First-fit → primeiro bloco disponível
Best-fit → o bloco que deixa menos espaço livre
Worst-fit → o maior bloco de espaço livre'''

from colorama import Fore, Style

cores = [Fore.RED, Fore.GREEN, Fore.BLUE]

itens = ["[x]", "[y]", "[z]"]

for cor, item in zip(cores, itens):
    texto_formatado = f"{cor}{item}{Style.RESET_ALL}"
    print(texto_formatado)
