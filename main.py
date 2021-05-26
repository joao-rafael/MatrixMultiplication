import math
import random

import create 
import graph
import naive
import strassen

# entrada exemplo 
x = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

y = [
  [5, 6, 2],
  [3, 2, 1],
  [1, 0, 1]
]

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
  matrixA = create.matrix(Kmax, Amin, Amax)
  matrixB = create.matrix(Kmax, Amin, Amax)
  result, timeNaive = naive.multiply(matrixA, matrixB)
  # put strassen here

  timelistNaive.append(timeNaive)
  # append strassen here

  i += 1

# add strassen to params in future
graph.mount(timelistNaive, R)

# function to show the plot
graph.plt.show()