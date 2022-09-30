import funciones_Cristinarey as funciones

def test_esMultiplo():
    assert funciones.esMultiplo(25,20) == 5

def test_Max():
    assert funciones.calcularMax([1,4,6,9]) == 9

def test_Min():
    assert funciones.calcularMin([2,7,5,3]) == 2

def test_Mcm():
    assert funciones.minimoComunMultiplo(10,5) / 5

def test_duplicar():
    assert funciones.duplicar(5) * 5