
from threading import Thread
from time import sleep
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
#print("End of operation.")

if __name__ =="__main__":
  rodar = Thread(target = execute_task)
  print("Starting task...")
  print("task is running. Se it!")
  rodar.start()
  rodar.join()
  print("Task is over!!!")
print("End of operation.")
respost = input("Wanna more? ")
if respost == 'Yes' or respost == "yes":
  repeat(execute_task)
else:
  print("Thanks for test my test code. Bye!")
