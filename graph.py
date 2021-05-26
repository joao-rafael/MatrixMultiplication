# importing the required module
import matplotlib.pyplot as plt
  
def mount(timeList, R):
  # naive values
  naive = timeList
  # x axis - numero de execucoes
  x = list(range(1, R+1))
  # y axis - tempo de execucao
  y = naive
    
  # plotting the points 
  plt.plot(x, y)
    
  # naming the x axis
  plt.xlabel('Ordem das Matrizes')
  # naming the y axis
  plt.ylabel('Tempo de Execução')
    
  # graph title
  plt.title('Gráfico de Execução')
  

