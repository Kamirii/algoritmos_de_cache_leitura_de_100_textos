import numpy as np
from random import randint, random
from time import perf_counter
from funcoes_simulacao import gera_numeros_probabilidade, media_aleatorio_tempo
from fifo import fifo
from lru import lru
from lfu import lfu

def simulate_fifo(inputs):
  media = 0
  miss = 0
  for i in range(len(inputs)):
    start = perf_counter()
    miss += fifo(inputs[i])
    stop = perf_counter()
    media += (stop - start)
  return media / len(inputs), miss


def simulate_lru(inputs):
  media = 0
  miss = 0
  for i in range(len(inputs)):
    start = perf_counter()
    miss += lru(inputs[i])
    stop = perf_counter()
    media += (stop - start)
  return media / len(inputs), miss


def simulate_lfu(inputs):
  media = 0
  miss = 0
  for i in range(len(inputs)):
    start = perf_counter()
    miss += lfu(inputs[i])
    stop = perf_counter()
    media += (stop - start)
  return media / len(inputs), miss


TAMANHO = 5

def simulate(n):
  with open("relatorio.txt", "a") as f:
    f.write("-" * 50)
    f.write("\nUSUÁRIO NÚMERO {}\n".format(n))
    
    # Simulate FIFO with pure random inputs
    f.write("=====FIRST IN FIRST OUT=====\n")
    aleatorio_puro = [randint(1, 100) for i in range(TAMANHO)]
    media_fi, miss_fi = simulate_fifo(aleatorio_puro)
    f.write("Aleatórios puros:{} segundos \n".format(media_fi))
    f.write("Cache miss {}\n".format(miss_fi))

    # Simulate FIFO with Poisson inputs
    aleatorio_poisson = np.random.poisson(lam=50, size=TAMANHO)
    media_fi_po, miss_fi_po = simulate_fifo(aleatorio_poisson)
    f.write("Números de poisson:{} segundos.\n".format(media_fi_po))
    f.write("Cache miss {}\n".format(miss_fi_po))

    # Simulate FIFO with random inputs and a given probability
    aleatorio_probabilidade = gera_numeros_probabilidade(TAMANHO, 0.33)
    media_fi_prob, miss_fi_prob = simulate_fifo(aleatorio_probabilidade)
    f.write("Aleatórios com mais probabilidade:{} segundos.\n".format(
      media_fi_prob))
    f.write("Cache miss {}\n".format(miss_fi_prob))
    
    f.write("=====LEAST FREQUENTLY USED ====\n")
    aleatorio_puro = [randint(1, 100) for i in range(TAMANHO)]
    media_lfu, miss_lfu = simulate_lfu(aleatorio_puro)
    f.write("Aleatórios puros:{} segundos \n".format(media_lfu))
    f.write("Cache miss {}\n".format(miss_lfu))

   
    aleatorio_poisson = np.random.poisson(lam=50, size=TAMANHO)
    media_lfu_po, media_lfu_po = simulate_lfu(aleatorio_poisson)
    f.write("Números de poisson:{} segundos.\n".format(media_lfu_po))
    f.write("Cache miss {}\n".format(media_lfu_po))

   
    aleatorio_probabilidade = gera_numeros_probabilidade(TAMANHO, 0.33)
    media_lfu_prob, miss_lfu_prob = simulate_lfu(aleatorio_probabilidade)
    f.write(
      "Aleatórios com mais probabilidade:{} segundos.\n".format(media_lfu_prob))
    f.write("Cache miss {}\n".format(miss_lfu_prob))

    f.write("=====LEAST RECENTLY USED ====\n")
    aleatorio_puro = [randint(1, 100) for i in range(TAMANHO)]
    media_lru, miss_lru = simulate_lru(aleatorio_puro)
    f.write("Aleatórios puros:{} segundos \n".format(media_lru))
    f.write("Cache miss {}\n".format(miss_lru))

    # Simulate FIFO with Poisson inputs
    aleatorio_poisson = np.random.poisson(lam=50, size=TAMANHO)
    media_lru_po, miss_lru_po = simulate_lru(aleatorio_poisson)
    f.write("Números de poisson:{} segundos.\n".format(media_lru_po))
    f.write("Cache miss {}\n".format(miss_lru_po))

    # Simulate FIFO with random inputs and a given probability
    aleatorio_probabilidade = gera_numeros_probabilidade(TAMANHO, 0.33)
    media_lru_prob, miss_lru_prob = simulate_lru(aleatorio_probabilidade)
    f.write(
      "Aleatórios com mais probabilidade:{} segundos.\n".format(media_lru_prob))
    f.write("Cache miss {}\n".format(miss_lru_prob))

    resultado_fifo = media_aleatorio_tempo(media_fi,media_fi_po,media_fi_prob)
    resultado_lfu =  media_aleatorio_tempo(media_lfu,media_lfu_po,media_lfu_prob)
    resultado_lru =  media_aleatorio_tempo(media_lru,media_lru_po,media_lru_prob)

  return resultado_fifo,resultado_lfu,resultado_lru 