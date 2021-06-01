import fileinput

import matrix
import execution
import graph
import naive
import strassen

print("Multiplicação de Matrizes")
print("Desenvolvido por João Rafael")
print("O arquivo de entrada deve se chamar 'in.txt'")

# timelist 
timelistNaive = []
timelistStrassen = []
orderlist = []

# entrada de dados por arquivo
indata = []
for line in fileinput.input(files='in.txt'):
  indata.append(line.rstrip('\n'))

interval = indata[2].split(' ')
del indata[-1]
Amin, Amax = interval
Kmax, R = indata

# casting
Kmax = int(Kmax)
R = int(R)
Amin = int(Amin)
Amax = int(Amax)

k = 5


# loop de execução
i = 0
while i < R:
  
  # criação de matrizes
  power = 2 ** k;
  matrixA = matrix.createRandom(power, Amin, Amax)
  matrixB = matrix.createRandom(power, Amin, Amax)
  result, timeNaive = naive.multiply(matrixA, matrixB)

  # Strassen é recursivo, preciso contar o tempo fora da função
  timeStrassen = 0
  st = execution.start()
  resultStrassen = strassen.multiply(matrixA, matrixB, k)
  stend = execution.end()
  timeStrassen = execution.getTime(st, stend) 

  # dados para o gráfico
  timelistNaive.append(timeNaive)
  timelistStrassen.append(timeStrassen)
  orderlist.append(k)

  if(Kmax > 5 and k < Kmax):
    k += 1
  i += 1

# grafico
graph.mount(timelistNaive, timelistStrassen,  orderlist)

