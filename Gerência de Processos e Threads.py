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
