# cria matriz vazia 
def createResult(n, m):
  result = []

  for c in range(n):
    result.append([])

    for d in range(m):
      result[c].append(0)

  return result

#multiplica matriz
def multiply(a, b):
  result = createResult(len(a), len(b[0]))

  #itera sob as linhas de a
  for i in range(len(a)):

    #colunas de b, apenas para o primeiro elemento
    for j in range(len(b[0])):

      for k in range(len(b)):
        
        result[i][j] += a[i][k] * b[k][j]


  return result
   