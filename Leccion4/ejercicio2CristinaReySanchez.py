# Devuelve si un número es primo o no.
def esPrimo(numero):
  for i in range(2,numero):
    if (numero%i) == 0:
      return False
  return True

lista = [3, 4, 8, 5, 5, 22, 13]

# Filtra una lista, pasandole como primer parámetro en este caso el método es Primo,
# y como segundo paráemtro la lista
primos = list(filter(esPrimo, lista))

print(primos)