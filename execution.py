# calculo do tempo de execução
import time

def start():
  st = time.time()
  return st

def end():
  nd = time.time()
  return nd

def getTime(st, nd):
  return nd - st