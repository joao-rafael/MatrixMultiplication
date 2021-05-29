import math
import matrix

def multiply(m1, m2, k):

  ## divisao de matrizes
  sm1, sm2, sm3, sm4 = matrix.divide(m1)
  sm5, sm6, sm7, sm8 = matrix.divide(m2)

  ## recursao
  r1 = multiply(sm1, matrix.subtract(sm6, sm8), k/2)

  r2 = multiply(sm1, matrix.subtract(sm6, sm8), k/2)

  ## matriz resultante
  result = matrix.createEmpty()


  return result