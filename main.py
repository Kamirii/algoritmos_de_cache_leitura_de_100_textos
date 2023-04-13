from file_manager import deleta_textos,cria_textos,procura_texto
from simulacao import simulate

#cria_textos()
#deleta_textos()

while True:
    print("Insira um número de arquivo ou 0:")
    user = input()
    if user == '-1':
       fifo1,lfu1,lru1 = simulate(1)
       fifo2,lfu2,lru2 = simulate(2)
       fifo3,lfu3,lru3 = simulate(3)

       with open('relatorio.txt', 'a') as f:
        f.write("-"*50)
        f.write("\nMÉDIA DE TEMPO DAS CHAMADAS ALEÁTORIAS DE CADA ALGORITMO PARA OS 3 USUÁRIOS\n\n") 

        f.write("=====FIRST IN FIRST OUT=====\n")
        f.write("USER 1: {} segundos \n".format(fifo1))
        f.write("USER 2: {} segundos \n".format(fifo2))
        f.write("USER 3: {} segundos \n".format(fifo3))
        f.write('-'*50)
        f.write("\n=====LEAST FREQUENTLY USED=====\n")
        f.write("USER 1: {} segundos \n".format(lfu1))
        f.write("USER 2: {} segundos \n".format(lfu2))
        f.write("USER 3: {} segundos \n".format(lfu3))
        f.write('-'*50)
        f.write("\n=====LEAST RECENTLY USED=====\n")
        f.write("USER 1: {} segundos \n".format(lru1))
        f.write("USER 2: {} segundos \n".format(lru2))
        f.write("USER 3: {} segundos \n".format(lru3))
        f.write('-'*50)
        f.write("\n=====MÉDIA GERAL=====\n")
        f.write("FIFO:{} \n".format(fifo1+fifo2+fifo3))
        f.write("LFU: {} \n".format(lfu1+lfu2+lfu3))
        f.write("LRU: {} \n".format(lru1+lru2+lru3))
       continue
    elif user == '0':
      print('programa encerrado.')
      break
      
    procura_texto(user)



 


