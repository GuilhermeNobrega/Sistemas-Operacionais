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
