import glob 
import os 

def deleta_textos():
  filepath = glob.glob("textos/*.txt")
  
  for file in filepath:
    try:
      os.remove(file)
    except:
      print('erro')

def cria_textos():
  folder_name = 'textos'
  os.makedirs(folder_name, exist_ok=True)
  
  with open('texto_original/iliada.txt') as f:
      words = []
      i = 0
      for line in f:
          for word in line.split():
              words.append(word)
              i += 1
              if len(words) == 1000 and i // 1000 <= 100:
                  file_name = '{}.txt'.format(i // 1000)
                  file_path = os.path.join(folder_name, file_name)
                  with open(file_path, 'w') as out:
                      print(' '.join(words), file=out)
                  words = []


def conta_palavras(f):
    print("Total de palavras no arquivo")
  

def procura_texto(numero):
  path = glob.glob('textos/{}.txt'.format(numero))
  file = open(path[0],'r')
  #conta_palavras(file.read())
  print(file.read())
  
  
      
def path_textos():
  hard_disk = []
  try:
    for txt in glob.glob('textos/*.txt'):
      hard_disk.append(txt)
  except:
    print('erro ao criar lista de caminhos')

  return hard_disk