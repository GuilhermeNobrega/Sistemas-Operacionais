"""Desenvolva um programa que simule o uso da alocação particionada dinâmica, 
com os algoritmos Best-fit, Worst-fit e First-fit.
Guilherme Nóbrega Gomes Dantas
Luisa Carreiro
Guilherme Henrique"""
def menorvalor(vlr):
    return min(vlr, key=lambda a: a['Value'])
#Um dicionário em Python não pode ter chaves duplicadas.
BestFit = [
    {"Processo": "a", "Value": 10},
    {"Processo": "b", "Value": 20},
    {"Processo": "c", "Value": 5}
]
def piorvalor(vlr):
    return max(vlr, key=lambda a: a['Value'])
#Um dicionário em Python não pode ter chaves duplicadas.
WorstFit = [
    {"Processo": "Delta", "Value": 150},
    {"Processo": "Omega", "Value": 36},
    {"Processo": "Alfa", "Value": 59}
]
def primeirovalor(vlr):
    #return (vlr, key=lambda a: a['Value'])
#Um dicionário em Python não pode ter chaves duplicadas.
    return FirstFit[0]
FirstFit = [
    {"Processo": "Sacturn", "Value": 200},
    {"Processo": "Blackhole", "Value": 24},
    {"Processo": "Blackenerg", "Value": 69}
]
while True:

  escolha = int(input("""Qual você deseja escolher?
  [1] - BestFit
  [2] - WorstFit
  [3] - FirstFit
  [0] - Exit\n"""))

  if escolha == 0:
    print("The simulation is over..")
    break
  if escolha == 1:
    menor_valor = menorvalor(BestFit)
    print(menor_valor)
    x = 15
    salvar = menor_valor['Value']
    resultado = (x-salvar)
    #print(resultado)
    print(f"Processo x com valor {x} irá ser adicionado a menor posição de memória: => {menor_valor}")
    menor_valor.update({'Value': resultado})
    print(menor_valor)

  if escolha == 2:
    menor_valor = piorvalor(WorstFit)
    print(menor_valor)
    z = 50
    salvar = menor_valor['Value']
    resultado = (z-salvar)
    #print(resultado)
    print(f"Processo x com valor {z} irá ser adicionado a menor posição de memória: => {menor_valor}")
    menor_valor.update({'Value': resultado})
    print(menor_valor)

  if escolha == 3:
    index = None
    quadrado = primeirovalor(FirstFit)
    if "Value" in quadrado:
      index = list(FirstFit[0]).index("Value")
      print("Index of fee:", index) 
      menor_valor = primeirovalor(FirstFit)
      print(menor_valor)
      x = 67
      salvar = menor_valor['Value']
      #resultado = (x-salvar)
      #print(resultado)
      print(f"Processo x com valor {x} irá ser adicionado a menor posição de memória: => {salvar}")
      menor_valor.update({'Value': salvar-67})
      print(menor_valor)
