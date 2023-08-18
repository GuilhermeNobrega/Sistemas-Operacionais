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
    print(f"\t================OPERATING AT PROCESS TREE:============= =>: {contador}MB/s\n")
    sleep(1)
  
def repeat(execute_task):
  rodar = Thread(target = execute_task)
  rodar.start()
  rodar.join()
print("\t\t-------------STARTING OPERATION--------------\n")
while True:
    execute_task()
    redutor = memoria_total-1
    memoria_total = redutor
    print(f"PROCESSO {contador} EM EXECUÇÃO! CADA PROCESSO OCUPARÁ 1 DA MEMORIA TOTAL, QUE TEM POR CAPACIDADE TOTAL {memoria_total}\n")
    contador +=1
    memoria_ocupada_processos +=1
    if memoria_ocupada_processos == memoria_total:
      print("===============================QUANTIDADE DE MEMORIA TOTAL OCUPADA. O SISTEMA IRÁ PARAR AS EXECUÇÕES PARA EVITAR UM DEADLOCK!==============================\n")
      resposta = input("""===================DESEJA INTERROMPER AS EXECUÇÕES?=================================\n
      OPTION: [Yes]
      OPTION: [No]\n""")
      if resposta =='Yes' or resposta =='yes':
        print("\t\t------------SYSTEM INTERRUPTED----------\n")
        break
      else:
        print("\t\t============= [FATAL ERROR] UNEXPECTED CATASTROPHIC FAILURE!!=============\n")
        break
