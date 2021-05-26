
def multiply(a, b):
  print(a)
  result = [[]]

  #itera sob as linhas de a
  for i in range(len(a)):

    #colunas de b
    for j in range(len(b)):

      for k in range(len(b)):
        
        result[i][j] += a[i][k] * b[k][j]


  return result
   