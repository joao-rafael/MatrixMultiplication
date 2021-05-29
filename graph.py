# importa matplotlib
import matplotlib.pyplot as plt
  
def mount(timeList, R):
  # valores da naive multiplication
  naive = timeList
  # eixo x - ordem das matrizes por hora com numero de execucoes
  x = list(range(1, R+1))
  # eixo y - tempo de execucao
  y = naive
    
  # gera linha
  plt.plot(x, y)
    
  # nome do eixo x
  plt.xlabel('Ordem das Matrizes')
  # nome do eixo y
  plt.ylabel('Tempo de Execução')
    
  # título do gráfico
  plt.title('Gráfico de Execução')
  

