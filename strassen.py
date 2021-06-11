import matrix
import execution
import naive

# conta tempo -> strassen -> retorna resultado e tempo
def init(m1, m2, k): 
  # inicia contagem de tempo antes de multiplicar
  st = execution.start()
  result = multiply(m1, m2, k)
  stend = execution.end()
  timeStrassen = execution.getTime(st, stend) 

  return result, timeStrassen

# multiplicação de strassen
def multiply(m1, m2, k):
  # casting
  k = int(k)
  
  # condição de parada, se não as matrizes
  # ficariam arbitrariamente pequenas
  if k == 32 or k < 32:
    result = naive.multiply(m1, m2)[0]
    return result

  else:
    # divisao de matrizes - sm para sub matriz
    sm1, sm2, sm3, sm4 = matrix.divide(m1)
    sm5, sm6, sm7, sm8 = matrix.divide(m2)
    
    # recursão - cálculo p1 a p7
    p1 = multiply(sm1, matrix.subtract(sm6, sm8), k//2)

    p2 = multiply(matrix.sum(sm1, sm2), sm8, k//2)

    p3 = multiply(matrix.sum(sm3, sm4), sm5, k//2)

    p4 = multiply(sm4, matrix.subtract(sm7, sm5), k//2)

    p5 = multiply(matrix.sum(sm1, sm4), matrix.sum(sm5, sm8), k//2)

    p6 = multiply(matrix.subtract(sm2, sm4), matrix.sum(sm7, sm8), k//2)

    p7 = multiply(matrix.subtract(sm1, sm3), matrix.sum(sm5, sm6), k//2)

    # calculo dos elementos Cij - matriz resultante
    
    c11 = matrix.sum(matrix.subtract(matrix.sum(p5, p4), p2), p6)

    c12 = matrix.sum(p1, p2)

    c21 = matrix.sum(p3, p4)

    c22 = matrix.sum(matrix.subtract(matrix.subtract(p5, p3), p7), p1)

    # matriz resultante - com dimensão do tamanho dos elementos c
    result = matrix.createEmpty(len(c11)*2, len(c11)*2)

    # atribuicão
    for i in range (len(c11)):
      for j in range (len(c11)):
        result[i][j] = c11[i][j]
        result[i][j+len(c11)] = c12[i][j]
        result[i+len(c11)][j] = c21[i][j]
        result[i+len(c11)][j+len(c11)] = c22[i][j]

    return result