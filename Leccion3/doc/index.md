
##Definimos errores personalizados
```
class ErrorNumeroColumnas(Exception):
    def __init__(self, value):
        self.value = value

class ErrorMesSinContenido(Exception):
    def __init__(self, value):
            self.value = value
```

##Valida el dato proporcionado como parametro
```
def validarDato(dato, mes):
    if not(dato.replace('\'', '').lstrip('-').isnumeric()):
        raise ValueError('El valor \'' + dato + '\' del mes ' + mes + ' no es válido')
    if not(dato.lstrip('-').isnumeric()):
        raise ValueError('El valor \'' + dato + '\' del mes ' + mes + ' no es válido, pero como se puede traducir a un número lo damos por válido eliminando las comillas')
```

    
##Método que valida los datos de todos los meses
```
def validarTodosLosDatos(df):
    for mes in df.columns:
        try:
            for fila in df.index:
                valorFila = df[mes][fila]
                validarDato(valorFila, mes)
        except ValueError as error:
            print(error)
            continue
```

##Inicializa el dataframe obteniendo los datos del csv para sanitizarlos y generar un nuevo dataframe con dichos datos.
```
def inicializarDataFrame():
    #Cargamos el fichero sin depurar
    dfToClean = pd.read_csv('./finanzas2020.csv')

    #Obtener nombres columnas:
    headers = ''.join(dfToClean.columns.values).split('\t')

    if(len(headers)!=12):
        raise ErrorNumeroColumnas('El csv debe tener 12 columnas.')

    #Creamos un nuevo DataFrame el cual almacenará los datos depurados.
    dfClean = pd.DataFrame(columns=headers)

    #Recorremos cada row
    for row in dfToClean.itertuples():

        #Obtenemos los valores para cada fila
        valueCleaned = row[1].split('\t')

        #Asignamos los valores a la nueva tabla
        dfClean.loc[row.Index] = valueCleaned
    
    #Validamos que todos los meses tengan contenido al inicio de obtener el dateFrame.
    for mes in dfClean.columns:
        if not(tieneContenido(dfClean, mes)):
            raise ErrorMesSinContenido('El mes ' + mes + ' no tiene contenido.')

        
    #Si el archivo es encontrado, tiene 12 columnas y además tienen contenido devolvemos el dataFrame saneado.
    return dfClean

```

##Devuelve si el mes tiene al menos una fila informada.
```
def tieneContenido(df, mes):
    for fila in df.index:

        valorFila = df[mes][fila]

        if (valorFila != ''):
            return True
         
    return False
```


##Calcula los gastos del mes
```
def calcularGastosMensual(df, mes):
    gastosMes = 0
    for fila in df.index:

        valorFila = df[mes][fila]

        if not(tieneContenido(df,mes)):
            raise ValidationErr

        if ('-' in valorFila):

            valorLimpio = valorFila.replace('\'', '').lstrip('-')

            if (valorLimpio.isnumeric()):
                gastosMes += int(valorLimpio)
         
    return gastosMes
```
##Calcula los ingresos del mes
```
def calcularIngresosMensual(df, mes):
    ingresosMes = 0
    for fila in df.index:

        valorFila = df[mes][fila]

        valorLimpio = valorFila.replace('\'', '')

        ##El isnumeric ignora de por si los negativos.
        if (valorLimpio.isnumeric()):

            ingresosMes += int(valorLimpio)
         
    return ingresosMes
```
##Calcula el mes con más gastos
```
def calcularMesMasGastos(df):

    maximoGastado = 0
    mesMasGastado = ''

    for mes in df.columns:
        
        gastos = calcularGastosMensual(df, mes)

        if (maximoGastado < gastos):
            maximoGastado = gastos
            mesMasGastado = mes

    print('Maximo gastos: ' + str(maximoGastado))
    print('Mes máximo gastos: ' + mesMasGastado)
```
##Calcular el mes con más ahorro
```
def calcularMesMasAhorro(df):

    maximoAhorro = 0
    mesMasAhorro = ''

    for mes in df.columns:
        
        ingresos = calcularIngresosMensual(df, mes)
        gastos = calcularGastosMensual(df, mes)

        ahorro = ingresos - gastos
    
        if (maximoAhorro < ahorro):
            maximoAhorro = ahorro
            mesMasAhorro = mes

    print('Máximo ahorro: ' + str(maximoAhorro))
    print('Mes máximo ahorro: ' + mesMasAhorro)
```

##Calcular media gastos
```
def mediaGastos(df):
    total = 0

    for mes in df.columns:
        total += calcularGastosMensual(df, mes)
    
    print('La media de gastos es ' + str(total/len(df.columns)))
```
##Calcular gasto Total del año
```
def gastoTotal(df):
    total = 0

    for mes in df.columns:
        total += calcularGastosMensual(df, mes)

    print('El gasto total es: ' +  str(total))
```
##Calcular ingresos totales del año.
```
def ingresosTotal(df):
    total = 0

    for mes in df.columns:
        total += calcularIngresosMensual(df, mes)

    print('Ingresos total es: ' + str(total))
```


##Método que ejecuta todo el proceso.
```
def calcular():
    try:
        df = inicializarDataFrame()
        # validamos todos los datos
        validarTodosLosDatos(df)

        calcularMesMasGastos(df)
        calcularMesMasAhorro(df)
        mediaGastos(df)
        gastoTotal(df)
        ingresosTotal(df)

    except FileNotFoundError:
        print('El fichero no se ha encontrado.')
    except ErrorNumeroColumnas as error:
        print(error)
```