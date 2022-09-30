import pdb
pdb.set_trace()

# Devuelve el elemento máximo de la lista.
def devuelveMax(element):
    return max(element)

# Pinta por la terminal el valor máximo de las sublistas
def valorMaximoPorLista(lista):

    for element in lista:
        print(devuelveMax(element))


lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

valorMaximoPorLista(lista)
