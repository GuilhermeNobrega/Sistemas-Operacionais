#Gerência de Processos e Threads

#Problema 1: "Desenvolva um programa que simule a criação de processos e a alocação de recursos em um Sistema Operacional. Cada processo deve requerer recursos específicos, e o programa deve garantir que nenhum processo entre em deadlock."

lista_processos = [];
memoria_total = 5
memoria_ocupada_processos = 0
contador = 0
while True:
  resposta = input("Deseja adicionar mais um processo?")
  if resposta == 'sim':
    redutor = memoria_total-1
    memoria_total = redutor
    print(f"PROCESSO {contador} EM EXECUÇÃO! CADA PROCESSO OCUPARÁ 1 DA MEMORIA TOTAL, QUE TEM POR CAPACIDADE TOTAL {memoria_total}")
    contador +=1
    memoria_ocupada_processos +=1
    if memoria_ocupada_processos == memoria_total:
      print("QUANTIDADE DE MEMORIA QUEBRADA!")
      break




#codigo novo
#Gerência de Processos e Threads

#Problema 1: "Desenvolva um programa que simule a criação de processos e a alocação de recursos em um Sistema Operacional. Cada processo deve requerer recursos específicos, e o programa deve garantir que nenhum processo entre em deadlock."
from threading import Thread
from time import sleep
lista_processos = [];
memoria_total = 10
memoria_ocupada_processos = 0
contador = 0
def execute_task():
  contador= 0
  valor = 5
  for contador in range(valor):
    print(f"\tCreating some tasks: =>: {contador}\n")
    sleep(1)
  
def repeat(execute_task):
  rodar = Thread(target = execute_task)
  print("Starting task...")
  print("task is running. Se it!")
  rodar.start()
  rodar.join()
  print("Task is over!!!")
while True:
    execute_task()
    redutor = memoria_total-1
    memoria_total = redutor
    print(f"PROCESSO {contador} EM EXECUÇÃO! CADA PROCESSO OCUPARÁ 1 DA MEMORIA TOTAL, QUE TEM POR CAPACIDADE TOTAL {memoria_total}")
    contador +=1
    memoria_ocupada_processos +=1
    if memoria_ocupada_processos == memoria_total:
      print("QUANTIDADE DE MEMORIA TOTAL OCUPADA. O SISTEMA IRÁ PARAR AS EXECUÇÕES PARA EVITAR UM DEADLOCK!")
      resposta = input("DESEJA INTERROMPER AS EXECUÇÕES?")
      if resposta =='sim' or resposta =='Sim':
        print("------------SISTEMA INTERROMPIDO----------")
        break
      else:
        print("Fuck you dude")
        break
