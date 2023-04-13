from random import random,randint

def gera_numeros_probabilidade(num_samples,probabilidade):
  numbers = []
  for i in range(num_samples):
    if random() < probabilidade:
      numbers.append(randint(30, 40))
    else:
      numbers.append(randint(1, 29) if random() < 0.5 else randint(41, 100))
  return numbers

def media_aleatorio_tempo(valor1,valor2,valor3):
  resultado = (valor1+valor2+valor3)/(3)
  return resultado

