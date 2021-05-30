# multiplicacao naive
import execution
import matrix

#multiplica matriz
def multiply(a, b):
  start = execution.start()

  result = matrix.createEmpty(len(a), len(b[0]))

  #itera sob as linhas de a
  for i in range(len(a)):

    #colunas de b, apenas para o primeiro elemento
    for j in range(len(b[0])):

      for k in range(len(b)):
        
        result[i][j] += a[i][k] * b[k][j]

  end = execution.end()
  executionTime = execution.getTime(start, end)
  
  return result, executionTime
  