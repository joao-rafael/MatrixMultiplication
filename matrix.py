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

  for i in range (len(m1)):
    line = []

    for j in range (len(m1[0])):
      line.append(m1[i][j] + m2[i][j])

    result.append(line)

  return result

# subtrai matrizes
def subtract(m1, m2):
  result = []

  for i in range (len(m1)):
    line = []

    for j in range (len(m1[0])):
      line.append(m1[i][j] - m2[i][j])

    result.append(line)
  
  return result

    
# divide uma matriz em quatro
def divide(matrix):
  m1 = m2 = m3 = m4 = matrix

  while len(m1) > len(matrix)/2:
    m1 = m1[:len(m1)//2]
    m2 = m2[:len(m2)//2]
    m3 = m3[len(m3)//2:]
    m4 = m4[len(m4)//2:]

  while len(m1[0]) > len(matrix[0])//2:
    for i in range(len(m1[0])//2):
      m1[i] = m1[i][:len(m1[i])//2]
      m2[i] = m2[i][len(m2[i])//2:]
      m3[i] = m3[i][:len(m3[i])//2]
      m4[i] = m4[i][len(m4[i])//2:]

  return m1, m2, m3, m4

