# operações de matrizes

import random

# cria matriz com valores zero
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
def sum(m1, m2):
  result = []
  n = len(m1)

  for i in range (0, n):
    line = []

    for j in range (0, n):
      line.append(m1[i][j] + m2[i][j])

    result.append(line)

  return result

# subtrai matrizes
def subtract(m1, m2):
  result = []
  n = len(m1)
  
  for i in range (0, n):
    line = []
    for j in range (0, n):
      line.append(m1[i][j] - m2[i][j])

    result.append(line)

  return result

    
# divide uma matriz em quatro
def divide(matrix):
  n = len(matrix)//2

  a = createEmpty(n,n)
  b = createEmpty(n,n)
  c = createEmpty(n,n)
  d = createEmpty(n,n)

  for i in range(0, n):
    for j in range(0, n):

      a[i][j] = matrix[i][j]
      b[i][j] = matrix[i][j+n]
      c[i][j] = matrix[i+n][j]
      d[i][j] = matrix[i+n][j+n]

  return a, b, c, d

