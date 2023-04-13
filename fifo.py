from queue import Queue
import random 

files_cache = Queue(maxsize=10)

def fifo(user):
  file_name = f"textos/{user}.txt"  
  tempQueue = Queue() 
                    
  if (0 < int(user) <= 100):
    while not files_cache.empty():
      item = files_cache.get()
      first_string = item[0]
      tempQueue.put(item)
      if first_string == file_name:
        while not tempQueue.empty():
          files_cache.put(tempQueue.get())
        print(item)
        #pega da memoria cache
        return 0
        
        
    while not tempQueue.empty():
      files_cache.put(tempQueue.get())
    #coloca um item na filas
    if (files_cache.full() == False):
      with open(file_name, "r") as arquivo:
        conteudo = arquivo.read()
        files_cache.put((file_name, conteudo))
        print((file_name,conteudo))
        # Adiciona o nome do arquivo e o conteúdo à fila 
        return 1
    else:
      #tira o ultimo item da lista
      files_cache.get(0)
      file_name = f"textos/{user}.txt"
      with open(file_name, "r") as arquivo:
        conteudo = arquivo.read()
        files_cache.put((file_name))
        print((file_name,conteudo))
        return 0
        
  else:
    print("número inválido")
    return 0 


