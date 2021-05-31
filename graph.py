# importa matplotlib
import matplotlib.pyplot as plt
  
def mount(timeListNaive, timeListStrassen, R):
  # valores da naive multiplication
  naive = timeListNaive
  strassen = timeListStrassen

  # eixo x - ordem das matrizes por hora com numero de execucoes
  x = list(range(1, R+1))
  # eixo y - tempo de execucao
  y = naive
    
  x1 = list(range(1, R+1))
  y1 = strassen
  # gera linha
  plt.plot(x, y, label='Naive')
  plt.plot(x1, y1, label='Strassen')

  # nome do eixo x
  plt.xlabel('Ordem das Matrizes')
  # nome do eixo y
  plt.ylabel('Tempo de Execução')
    
  # título do gráfico
  plt.title('Gráfico de Execução')
