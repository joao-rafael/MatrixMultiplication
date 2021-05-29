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

# entrada de dados:
Kmax, R, Amin, Amax = input().split(" ")
Kmax = int(Kmax)
R = int(R)
Amin = int(Amin)
Amax = int(Amax)

#loop de execução
i = 0
while i < R:
  matrixA = matrix.createRandom(Kmax, Amin, Amax)
  matrixB = matrix.createRandom(Kmax, Amin, Amax)
  result, timeNaive = naive.multiply(matrixA, matrixB)
  # put strassen here

  timelistNaive.append(timeNaive)
  # append strassen here

  i += 1

# add strassen to params in future
graph.mount(timelistNaive, R)

# function to show the plot
graph.plt.show()