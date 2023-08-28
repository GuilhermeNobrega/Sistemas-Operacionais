"""Desenvolva um programa que simule o uso da alocação particionada dinâmica, 
com os algoritmos Best-fit, Worst-fit e First-fit."""

def menorvalor(vlr):
    return min(vlr, key=lambda d: d['Value'])
#Um dicionário em Python não pode ter chaves duplicadas.
BestFit = [
    {"Processo": "a", "Value": 10},
    {"Processo": "b", "Value": 20},
    {"Processo": "c", "Value": 5}
]

menor_valor = menorvalor(BestFit)
print(menor_valor)
x = 15
salvar = (menor_valor['Value'])
print(x-salvar)
