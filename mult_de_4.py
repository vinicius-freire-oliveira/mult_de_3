# Lista gerada
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# declarando a lista de multiplos de 4 
mult_4 = []
# função para gerar uma lista dos múltiplos de 4 a partir de uma lista
def multiplo_4(lista: list) -> list:
  for i in range(len(lista)):
    # condição para um número ser múltiplo de 4
    if lista[i] % 4 == 0:
      mult_4.append(lista[i])
  return mult_4

# retornando a lista gerada para a variável mult_4
mult_4 = multiplo_4(lista)
print(mult_4)
