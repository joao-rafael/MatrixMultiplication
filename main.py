import getInput
import matrix
import execution
import graph
import naive
import strassen

print("Multiplicação de Matrizes")
print("Desenvolvido por João Rafael")
print("Para alterar a entrada, alterar o arquivo 'in.txt'")
print("Ps.: apesar de ter sido otimizado, ainda demora bastante.")

# timelist 
timelistNaive = []
timelistStrassen = []
orderlist = []

# valores de entrada
Amin, Amax, Kmax, R = getInput.main()

# variáveis auxiliares
k = 5
i = 0
flag = False

# loop de execução
while i < R:
  
  # criação de matrizes
  power = 2 ** k;
  matrixA = matrix.createRandom(power, Amin, Amax)
  matrixB = matrix.createRandom(power, Amin, Amax)

  # multiplicação das matrizes
  result, timeNaive = naive.multiply(matrixA, matrixB)
  resultStrassen, timeStrassen = strassen.init(matrixA, matrixB, power)
  
  # dados para o gráfico
  if(flag == False):
    # primeira iteração até a ordem 2^Kmax (de 32 até Kmax)
    timelistNaive.append(timeNaive)
    timelistStrassen.append(timeStrassen)
    orderlist.append(k)
  else:
    # Kmax Atingido, valores agora são media de tempo de execução de cada ordem
    timelistNaive[k-5] = (timelistNaive[k-5] + timeNaive) / 2
    timelistStrassen[k-5] = (timelistStrassen[k-5] + timeStrassen) / 2
  

  # reset de k caso Kmax seja atingido - acelera muito.
  if(k == Kmax):
    k = 5
    flag = True

  # enquanto k for menor que kmax, incrementa k para
  # executar matrizes de ordens diferentes
  if(Kmax > 5 and k <= Kmax):
    k += 1

  # print de dados de cada execução
  print("*****************")
  print("Executado: matriz de ordem " + str(power) + ".")
  print("Tempo de execução naive: " + str(timeNaive))
  print("Tempo de execução com o algoritmo de Strassen: " + str(timeStrassen))

  # incremento do loop
  i += 1

print("*****************")
# gráfico montado após execução
graph.mount(timelistNaive, timelistStrassen,  orderlist)