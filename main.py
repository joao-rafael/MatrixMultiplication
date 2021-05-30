import math
import random

import matrix
import graph
import naive
import strassen

print("Multiplicação de Matrizes")
print("Insira dados:")

# timelist 
timelistNaive = []
timelistStrassen = []
orderlist = []

# entrada de dados:
Kmax, R, Amin, Amax = input().split(" ")
Kmax = int(Kmax)
R = int(R)
Amin = int(Amin)
Amax = int(Amax)

k = 5
#loop de execução
i = 0
while i < R:
  if(Kmax > 5 and k < Kmax):
    k += 1
  matrixA = matrix.createRandom(k, Amin, Amax)
  matrixB = matrix.createRandom(k, Amin, Amax)
  result, timeNaive = naive.multiply(matrixA, matrixB)
  resultStrassen, timeStrassen = strassen.multiply(matrixA, matrixB, k)


  timelistNaive.append(timeNaive)
  timelistStrassen.append(timeStrassen)
  orderlist.append(k)
  i += 1

# add strassen to params in future
graph.mount(timelistNaive, timelistStrassen,  R)

# function to show the plot
graph.plt.show()