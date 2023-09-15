from threading import Thread
from time import sleep
def task():
  sleep(1)
  print("doing..?")

if __name__ =="__main__":
  work = Thread(target=task)
  work.start()
  print("Task will  run!")
  work.join()
print("task is over..")




from threading import Thread
from time import sleep
def execute_task():
  contador= 0
  valor = 5
  for contador in range(valor):
    print("Creating some tasks")


if __name__ =="__main__":
  rodar = Thread(target = execute_task)
  print("Starting task...")
  rodar.start()
  print("task is running. Se it!")
  rodar.join()
  print("Task is over!!!")
print("End of tape..?")
