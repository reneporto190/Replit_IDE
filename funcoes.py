def somar():
  print('Funcao somar.')

def multiplicar():
  print('Funcao multiplicar.')

def find_index(to_find, item):
  for i, valor in enumerate(to_find):
    if valor == item:
      return i
  return -1