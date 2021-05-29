# operações de matrizes

import random

# cria matriz vazia 
def createEmpty(n, m):
  result = []

  for c in range(n):
    result.append([])

    for d in range(m):
      result[c].append(0)

  return result

# cria matriz com valores aleatórios
def createRandom(Kmax, Amin, Amax):
  matrix = []

  for c in range(Kmax):
    matrix.append([])

    for d in range(Kmax):
      matrix[c].append(random.randint(Amin, Amax))
  
  return matrix

# soma matrizes
def sum(a, b):
  return a + b

