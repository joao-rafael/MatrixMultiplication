import math

import graph
import naive

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
print(naive.multiply(x, y))

# function to show the plot
graph.plt.show()