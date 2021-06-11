# importa matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
  
def mount(timeListNaive, timeListStrassen, R):

  # valores da naive multiplication
  naive = timeListNaive
  strassen = timeListStrassen

  # eixo x - ordem das matrizes por hora com numero de execucoes
  x = R
  # eixo y - tempo de execucao
  y = naive
    
  x1 = R
  y1 = strassen
  # gera linha
  plt.plot(x, y, label="Naive")
  plt.plot(x1, y1, label="Strassen")
  plt.legend(loc="upper left")
  plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))

  # nome do eixo x
  plt.xlabel('Ordem das Matrizes - Expoentes de Potência base 2')
  # nome do eixo y
  plt.ylabel('Tempo de Execução - Segundos')
    
  # título do gráfico
  plt.title('Gráfico de Execução')

  print("Pressionar 'ctrl-C' para terminar execução.")

  plt.show()