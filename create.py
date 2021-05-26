import random

def matrix(Kmax, Amin, Amax):
  matrix = []

  for c in range(Kmax):
    matrix.append([])

    for d in range(Kmax):
      matrix[c].append(random.randint(Amin, Amax))
  
  return matrix