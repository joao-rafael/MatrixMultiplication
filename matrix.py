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
  if(len(m1) == 1):
    result = [m1[0] + m2[0]]
    return result
  else:
    for i in range (len(m1)):
      line = []

      for j in range (len(m1[0])):
        line.append(m1[i][j] + m2[i][j])

      result.append(line)

    return result

# subtrai matrizes
def subtract(m1, m2):
  result = []
  if(len(m1) == 1):
    result = [m1[0] - m2[0]]
    return result
  else:
    for i in range (len(m1)):
      line = []

      for j in range (len(m1[0])):
        line.append(m1[i][j] - m2[i][j])

      result.append(line)
    return result

    
# divide uma matriz em quatro
def divide(matrix):
  """Split matrix into quarters."""
  a = b = c = d = matrix

  while len(a) > len(matrix)/2:
      a = a[:len(a)//2]
      b = b[:len(b)//2]
      c = c[len(c)//2:]
      d = d[len(d)//2:]

  while len(a[0]) > len(matrix[0])//2:
      for i in range(len(a[0])//2):
          a[i] = a[i][:len(a[i])//2]
          b[i] = b[i][len(b[i])//2:]
          c[i] = c[i][:len(c[i])//2]
          d[i] = d[i][len(d[i])//2:]

  return a, b, c, d

