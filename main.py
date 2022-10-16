velocidade = 120

if velocidade > 110:
  print("Acima da velocidade")
  print("Reduza a velocidade")
elif velocidade <60:
  print("Favor dirigir acima de 80km/h")
else:
  print("Velocidade OK!")

renda_acima_5mil = True
Nome_limpo = True

if renda_acima_5mil and Nome_limpo:
  print("Financiamento aprovado!")
else:
  print("Financiamento Reprovado!")

## Operador tenario
idade = 16
if idade >= 16:
  resultado = print("Ela pode votar")
else:
  resultado = print("Voto nào Permitido.")

# Para o voto repetido si a idade for maior de 16
print(resultado)

# Tenario
resultado = 'Voto Permitido' if idade>=16 else "voto nao  Permitido"
print(resultado)

#For 
for numero in range(1,5):
  print(numero)

# for loops
palavra = 'Google'
for letra in palavra:
  print(f'{letra} + esta dentro da palavra {palavra}')

compra_confirmada = False
dados_compra = 'Compra no valor de R$ 12,50 e entrega confirmada'

for enviar in range(3):
  if compra_confirmada:
    print(dados_compra)
    print('Detalhes enviados para seu e-mail')
    break
else:
    print('Falha na compra')

# Nested loop, loop dentro do loop
for numero1 in range(1,6):
  print('Produto' + str(numero1))
  for numero2 in range(11):
    print(numero1,numero2)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

palavra = 'ESPECIAL'

for spaco in palavra:
  print(f' {spaco}' , end='')

print()
linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
  for c in range(colunas):
    print(simbolo, end='')
  print()

# taboada
#outer loop

for i in range(1,11):
  #nested loop
  #ot iterate from a to 10
  for j in range(1,11):
    #print multiplication
    print(f' - {i * j}', end=' ')
  print()

# While
  # cria uma promocao com desconto de valores.
valor = 100
dia = 1
while valor  > 20:
  dia += 1
  print(f' No dia {dia} o produto vai ser vendido por {valor}')
  print(valor)
  valor -= 5

#non default sempre na frente do default
def boas_vindas(nome,quantidade=6):
  print(f'Ola {nome}.')
  print(f'Temos {str(quantidade)} laptop em estoque')

boas_vindas('Rene',5)
boas_vindas('Dennis')
boas_vindas('Flavia',2)

# realiza uma tarefa, imprime n<ap guardo o valor na memoria
# calcula e retorna um valor. guarda o valor na memoria.

def cliente1(nome):
  print(f'Ola {nome}')


def cliente2(nome):
  return(f'Ola {nome}')

x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)

#Varios argumentos (xargs)

def soma(*numeros):
  resultado =0 
  for num in numeros:
    resultado += num
  return resultado

x = soma(2,3,4,7)

print(x)

#Varios argumentos (xxargs) define os parametos junto com os argumentos

def agencia(**carro):
  return carro

print(agencia(marca='gol',cor='Branca', motor=1.0, placa=1234))
print(agencia(marca='gol',cor='Azul', motor=1.0))
print(agencia(marca='gol',cor='Branca', motor=1.0, placa=14444))

import math

print(math.factorial(40))

print(math.floor(2.7))
print(math.ceil(2.7))

# Listas

cidades = ['Rio de Janeiro','Sao Paulo','Salvador','Goiania']

#subistitindo um item na lista
cidades[0]='Brasilia'

#Funcoes da lista

cidades.append('Recife')
cidades.insert(0,'Campinas')
cidades.remove('Salvador')
cidades.pop(0) #retirar
print(cidades)
#Contactenar listas
numeros =[1,2,3,4]
letras = ['a','b','C','d']
numeros.extend(letras)
print(numeros)

# Unpacking

produtos = [['arroz','feijao'],['laranja', 'banana']] 
print(produtos[0][1])

#Associar variaveis aos items da lista

produtos = ['arroz','feijao','laranja', 'banana',5,6,7,8]

item1, item2, item3, *outros, item8 = produtos
print(item1)
print(item2)
print(item8)
print(outros)

for x in produtos:
  print(x * 2)

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo','verde','azul','vermelho']

if cor_cliente.lower() in cores:
  print('Em estoque')
else:
  print('Nao temos esta cor en estoque')

# zip zipar duas listas
# nao e o mesmo que  contatenar duas listas, ele criou um tupla dentro s lista por index
cores = ['amarelo','verde','azul','vermelho']
valores= [10,20,30,40]

duas_listas = zip(valores,cores)

print(list(duas_listas))

import funcoes
#from funcoes import somar, multiplicar
#somar()
#multiplicar()

funcoes.somar()
funcoes.multiplicar()

# Package
from items.cadastro import cliente
cliente()

from funcoes import find_index
list1 = ['a','b','c','d']
var1 = find_index(list1, 'b')
print(var1)


# Criar uma lista de frutas a partir o input 

frutas_usuario = input('Digite o nome das frutas seprados por virgula: ')
frutas_lista = frutas_usuario.split(', ')
print(frutas_lista)

# Arrays conjunto de listas, trabalhar com listas grande. tipos de arrays, u(string, i (integer etc))

from array import array

letras1 = ['a','b','c','d']
numeros_I = [10,20,30,40]
numeros_f = [1.2,2.2,3.2]

letras1 = array('u',['a','b','c','d'])
numeros_i = array('i',[10,20,30,40])
numeros_f = array('f',[1.2,2.2,3.2])

print(letras)
print(numeros_i)
print(numeros_f)

# Sets (listas)
#Evita itens duplicados
# nào utiliza index

numeros_I = [10,20,30,40,50]
numeros_II = [10,20,30,40]

num1 = set(numeros_I)
num2 = set(numeros_II)

print(num1 | num2) # Union sem duplicados
print(num1 - num2) # Union elimina duplicados la lista num 1 com a lista num2
print(num1 ^ num2) # Symmetric difference uniào das duas linhas menos os identicos
print(num1 & num2) # And o que e duplicado em uma linha e na outra

s1= {1,2,3,4,5,6}
s1.add(7)
print(s1)
s1.update([6,7,8,9,10])
print(s1)
#s1.remove(1)
#s1.discart(2)

set1= {'a','b','c'}
set2= {'a','d','e'}
set3= {'c','d','f'}

set4 = set1.union(set2)
print(set4)
set4 = set1.difference(set3)
print(set4)
set4 = set1.intersection(set2)
print(set4)
set4 = set1.intesection(set2)
print(set4).