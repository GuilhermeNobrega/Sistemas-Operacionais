"""Desenvolva um programa que simule o uso da alocação particionada dinâmica, 
com os algoritmos Best-fit, Worst-fit e First-fit."""

def menorvalor(vlr):
    return min(vlr, key=lambda a: a['Value'])
#Um dicionário em Python não pode ter chaves duplicadas.
BestFit = [
    {"Processo": "a", "Value": 10},
    {"Processo": "b", "Value": 20},
    {"Processo": "c", "Value": 5}
]

menor_valor = menorvalor(BestFit)
print(menor_valor)
x = 15
salvar = menor_valor['Value']
resultado = (x-salvar)
#print(resultado)
print(f"Processo x com valor {x} irá ser adicionado a menor posição de memória: => {menor_valor}")
menor_valor.update({'Value': resultado})
print(menor_valor)
