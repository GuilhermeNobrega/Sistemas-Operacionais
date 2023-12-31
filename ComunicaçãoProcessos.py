"""Projeto do Sistema: Cada grupo deve projetar o sistema, considerando como os processos serão usados para criar, enviar e receber mensagens. Pense em como os processos se comunicarão uns com os outros.
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Implementação: Implemente uma versão simplificada do sistema de gerenciamento de mensagens. Use uma linguagem de programação ou ambiente de sua escolha. Certifique-se de que a comunicação entre processos seja eficiente e segura.
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Simulação: Simule o envio e a recepção de mensagens entre processos, demonstrando como o sistema lida com vários cenários, como mensagens de alta prioridade, mensagens em grupo, etc.
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Relatório: Prepare um relatório descrevendo a arquitetura do sistema, os mecanismos de comunicação de processos utilizados e quaisquer desafios enfrentados durante a implementação.
falta: ==>> fazer comunicação entre processos. Como será feito? A ideia é ver se um processo foi finalizado. Caso tenha sido, de maneira hipotetica, o outro processo poderá rodar, havendo uma comunicação e entre a memória
recebendo respostas e autorizando o outro processo começar a executar. Será dessa maneira que será implementado, faltando apenas essa parte e a explicação no relatório, para a finalização do projeto."""

from time import sleep
from random import choice
lista_nomes = ['ay1','bu3','g8s','j84','e3a','p9p','8cz','b4f','1q1','w3w','5ff','6fh','c6c','0o0','9iu','9n0','a4f','b87','a77',
'8z2','1z3','4z5','cv5','cv1','z9l','z0ç','Z3D','fk4','mt9','ar4','fm1','ct3','r31']
lista_processos = [];
memoria_total = 10
memoria_ocupada_processos = 0
def execute_task():
  valor = 5
  for contador in range(valor):
    PID = random.randint(200,15000)
    nombres = choice(lista_nomes)
    randoms = randint(50,200)
    print(f"\n\n\t================| OPERATING AT PROCESS | [{nombres.upper()}] | PID | [{PID}]:============= =>: {randoms}MB/s\n")
    randoms = randint(50,200)
    print(f"\t================| SUBPROCESS | :============= =>: {randoms}MB/s\n")
    sleep(1)
  

print("\t\t-------------STARTING OPERATION--------------\n")
c = 10
for d in range(c):
    sleep(0.5)
    print("\t-", end='')

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


#----------------------------------------------------------------

from time import sleep
import random
lista_nomes = ['ay1','bu3','g8s','j84','e3a','p9p','8cz','b4f','1q1','w3w','5ff','6fh','c6c','0o0','9iu','9n0','a4f','b87','a77',
'8z2','1z3','4z5','cv5','cv1','z9l','z0ç','Z3D','fk4','mt9','ar4','fm1','ct3','r31']
lista_Response = ['Yes','No']
contador = 0
lista_processos = [];
memoria_total = 10
memoria_ocupada_processos = 0
c = 10
BUFFER = 'BUFFER_EVENTS'
def execute_task():
  valor = 5
  for contador in range(valor):
    response = random.choice(lista_Response)
    PID = random.randint(200,15000)
    nombres = random.choice(lista_nomes)
    randoms = random.randint(50,200)
    print(f"\n\n\t================| OPERATING AT PROCESS | [{nombres.upper()}] | PID | [{PID}]:============= =>: {randoms}MB/s\n")
    randoms = random.randint(50,200)
    print(f"\t================| SUBPROCESS | :============= =>: {randoms}MB/s\n")
    for d in range(c):
      sleep(0.5)
      print(f"==== [SENDING INFORMATIONS TO BUFFER {BUFFER}] ====\n", end='')
      print(f"[X][X][X][X][X][X][X][X][X][X][X]")
    sleep(5)
    #x = str(input("PROCESS IS RUNNING?"))
    print(response)
    if(response=="Yes"):
      print(f"Necessário esperar o processo {nombres.upper()} com PID = [{PID}] finalizar...")
      sleep(5)
    else:
      print(f"PROCESSO {nombres.upper()}, CUJO PID É {PID} FINALIZADO! PRÓXIMO...")

print("\t\t-------------STARTING OPERATION--------------\n")
for d in range(c):
    sleep(0.5)
    print("\t-", end='')
execute_task()



#---------------------------------- atualizado 25/09

from time import sleep
import random
lista_nomes = ['ay1', 'bu3', 'g8s', 'j84', 'e3a', 'p9p', '8cz', 'b4f', '1q1', 'w3w', '5ff', '6fh', 'c6c', '0o0', '9iu', '9n0', 'a4f', 'b87', 'a77',
              '8z2', '1z3', '4z5', 'cv5', 'cv1', 'z9l', 'z0ç', 'Z3D', 'fk4', 'mt9', 'ar4', 'fm1', 'ct3', 'r31']
lista_response = ['Yes', 'No']
buffer_name = 'BUFFER_EVENTS'
box_incompletos = {}
box_completos = {}
def execute_task():
    valor = 5
    for _ in range(valor):
        response = random.choice(lista_response)
        pid = random.randint(200, 15000)
        nombre = random.choice(lista_nomes)
        random_speed = random.randint(50, 200)
        print(f"\n\n\t================| OPERATING AT PROCESS | [{nombre.upper()}] | PID | [{pid}]:============= =>: {random_speed}MB/s\n")
        random_speed = random.randint(50, 200)
        print(f"\t================| SUBPROCESS | :============= =>: {random_speed}MB/s\n")
        for _ in range(5):
            sleep(0.5)
            print(f"==== [SENDING INFORMATIONS TO BUFFER://{buffer_name}] ====\n", end='')
        sleep(5)
        print(f"\n\n\t================| VERIFICANDO PROCESS | [{nombre.upper()}] | PID | [{pid}]:============= =>: {random_speed}MB/s\n")
        for _ in range(10):
          sleep(1)
          print("\t*", end='')
        print(f"\n{response}")
        if response == "Yes":
            a = 'INCOMPLETO'
            print(f"\n\n\t================| PROCESSO | [{nombre.upper()}] | PID | [{pid}]: | STATUS: [INCOMPLETO]|================")
            print('')
            box_incompletos.update({'| PROCESSO |': nombre.upper(),'| PID |': pid,'| STATUS |':a})
            print(box_incompletos)
            sleep(5)
        else:
            a = 'COMPLETO'
            print(f"\n\n\t================| PROCESSO | [{nombre.upper()}] | PID | [{pid}]: | STATUS: [FINALIZADO]|================")
            box_completos.update({'| PROCESSO |': nombre.upper(),'| PID |': pid,'| STATUS |':a})
            #print(box_completos)
        for _ in range(5):
          listaa = []
          dict_copy = box_completos.copy()
          print(listaa.append(dict_copy))
print("\t\t-------------STARTING OPERATION--------------\n")
for _ in range(10):
    sleep(0.5)
    print("\t-", end='')

execute_task()

#---------------------------------------- Original atualizado ----------------------------------
from time import sleep
import random

lista_nomes = ['ay1', 'bu3', 'g8s', 'j84', 'e3a', 'p9p', '8cz', 'b4f', '1q1', 'w3w', '5ff', '6fh', 'c6c', '0o0', '9iu', '9n0', 'a4f', 'b87', 'a77',
              '8z2', '1z3', '4z5', 'cv5', 'cv1', 'z9l', 'z0ç', 'Z3D', 'fk4', 'mt9', 'ar4', 'fm1', 'ct3', 'r31']

lista_response = ['Yes', 'No']
buffer_name = 'BUFFER_EVENTS'
box_incompletos = []
box_completos = []

def execute_task():
    valor = 5
    for _ in range(valor):
        response = random.choice(lista_response)
        pid = random.randint(200, 15000)
        nombre = random.choice(lista_nomes)
        random_speed = random.randint(50, 200)
        
        print(f"\n\n\t================| OPERATING AT PROCESS | [{nombre.upper()}] | PID | [{pid}]:============= =>: {random_speed}MB/s\n")
        random_speed = random.randint(50, 200)
        print(f"\t================| SUBPROCESS | :============= =>: {random_speed}MB/s\n")
        
        for _ in range(5):
            sleep(0.5)
            print(f"==== [SENDING INFORMATIONS TO BUFFER://{buffer_name}] ====\n", end='')
        sleep(5)
        
        print(f"\n\n\t================| VERIFICANDO PROCESS | [{nombre.upper()}] | PID | [{pid}]:============= =>: {random_speed}MB/s\n")
        for _ in range(10):
            sleep(1)
            print("\t*", end='')
        print(f"\n{response}")
        
        if response == "No":
            a = 'INCOMPLETO'
            print(f"\n\n\t================| PROCESSO | [{nombre.upper()}] | PID | [{pid}]: | STATUS: [INCOMPLETO]|================\n")
            box_incompletos.append({'| PROCESSO |': nombre.upper(),'| PID |': pid,'| STATUS |':a})
            print(box_incompletos[-1])
            sleep(5)
        else:
            a = 'COMPLETO'
            print(f"\n\n\t================| PROCESSO | [{nombre.upper()}] | PID | [{pid}]: | STATUS: [FINALIZADO]|================\n")
            box_completos.append({'| PROCESSO |': nombre.upper(),'| PID |': pid,'| STATUS |':a})
            print('\n')
            
    if len(box_incompletos) == 0:
        print("SEM PROCESSOS EM HIBERNAÇÃO")
    else:
        print("AGORA VAMOS EXECUTAR, POR ORDEM OS PROCESSOS PARADOS ANTES!\n")
        while box_incompletos:
            processo_info = box_incompletos.pop(0)
            print(processo_info['| PROCESSO |'])
            print(f"\n\n\t================| PROCESSO EM HIBERNAÇÃO | [{processo_info['| PROCESSO |']}] | PID | [{processo_info['| PID |']}]: | STATUS: [FINALIZADO]|================\n")
        print("acabou")

print("\t\t-------------STARTING OPERATION--------------\n")
for _ in range(10):
    sleep(0.5)
    print("\t-", end='')

execute_task()

