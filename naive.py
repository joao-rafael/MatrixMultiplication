import time

# importação de arquivo
import matrix

#multiplica matriz
def multiply(a, b):
  start = time.time()

  result = matrix.createEmpty(len(a), len(b[0]))

  #itera sob as linhas de a
  for i in range(len(a)):

    #colunas de b, apenas para o primeiro elemento
    for j in range(len(b[0])):

      for k in range(len(b)):
        
        result[i][j] += a[i][k] * b[k][j]

  end = time.time()
  executionTime = end - start
  
  return result, executionTime
   