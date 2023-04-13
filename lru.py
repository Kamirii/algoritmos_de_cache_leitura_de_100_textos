#em um cache usando a política least recently used (LRU), quando o cache está cheio e um novo bloco de dados precisa ser carregado no cache, o bloco LRU (o bloco que não foi acessado há mais tempo) é trocado do cache para dar lugar ao novo bloco. O bloco trocado pode ser armazenado em um cache de nível inferior, na memória principal ou até mesmo na memória virtual.

from random import randint
from collections import OrderedDict

cache = OrderedDict()
MAX_CACHE_SIZE = 10

def lru(user):
  if (0 < int(user) <= 100):
    
    file_name = f"textos/{user}.txt"
  
    if user in cache:
      print(cache)
      cache.move_to_end(user)
      return 1
    else:
      with open(file_name, "r") as arquivo:
        conteudo = arquivo.read()
        cache[user] = conteudo  # carrega o texto na memória
        print(conteudo)
        return 1  # não estava no cache
       
      # swap memory can occur in Cache memory. O cache utiliza memória de outro lugar temporariamente quando o número excede 1
    if len(cache) > MAX_CACHE_SIZE:
      print('RETIRADO DO CACHE')
      cache.popitem(last=False)
      return 0
  else:
    print("Arquivo não encontrado")
    return 0
