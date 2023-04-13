
fileHashTable = {}
n = 1
MAX_SIZE_CACHE = 10

def lfu(user):
  
  file_name = f"textos/{user}.txt"
  searchKey = f"key_{user}"
  if (0 < int(user) <= 100):
    if searchKey in fileHashTable:
      print(fileHashTable[searchKey][0])
      fileHashTable[searchKey][1] += 1
      return 0
    elif len(fileHashTable) <= MAX_SIZE_CACHE:
      with open(file_name, "r") as arquivo:
        conteudo = arquivo.read()
        file_acess = [conteudo, n]
        fileHashTable[searchKey] = file_acess
        print(fileHashTable[searchKey][0])
      return 1
    else:
      # Remove the least frequently used file
      min_file = min(fileHashTable.items(), key=lambda x: x[1][1])
      del fileHashTable[min_file[0]]
      with open(file_name, "r") as arquivo:
        conteudo = arquivo.read()
        file_acess = [conteudo, n]
        fileHashTable[searchKey] = file_acess
        print(fileHashTable[searchKey][0])
      return 1
  else:
    print("número inválido")
    return 0
