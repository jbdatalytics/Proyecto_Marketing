import pandas as pd


def eda_preliminar(df):
    """
    Realiza un análisis exploratorio preliminar de un DataFrame.

    Muestra una muestra aleatoria de 5 filas, información general del DataFrame, 
    porcentaje de valores nulos por columna, número de filas duplicadas y 
    recuento de valores para las columnas categóricas.

    Parámetros:
    df (pd.DataFrame): DataFrame a analizar.

    Retorno:
    None
    """
    
    display(df.sample(5))
    
    print('-------------------------------------')

    print('INFO')

    display (df.info()) 

    print('-------------------------------------')

    print('NULOS')

    display (round(df.isnull().sum()/df.shape[0] *100, 2))

    print('-------------------------------------')

    print('DUPLICADOS')

    display (df.duplicated().sum())    

    print('-------------------------------------')

    print('VALUE COUNTS')

    for col in df.select_dtypes (include='O').columns:    
        print (df[col].value_counts())                 
        print('------------------------------------')
        

def valores_minus(df):    
    """
    Convierte todos los valores de las columnas categóricas (tipo 'O') a minúsculas.

    Itera sobre las columnas de tipo objeto del DataFrame y transforma sus valores 
    a minúsculas.

    Parámetros:
    df (pd.DataFrame): DataFrame cuyos valores en columnas categóricas serán convertidos a minúsculas.

    Retorno:
    pd.DataFrame: DataFrame con los valores de las columnas categóricas convertidos a minúsculas.
    """

    for col in df.select_dtypes(include='O'). columns:    # cambio a minúscula todo el contenido del dataframe
        df[col]=   df[col].str.lower()


def comas (df,lista_col):
    """
    Reemplaza las comas por puntos en las columnas especificadas y convierte los valores a tipo float.

    Itera sobre las columnas proporcionadas en la lista y reemplaza las comas por puntos 
    en sus valores, luego convierte esos valores a tipo float.

    Parámetros:
    df (pd.DataFrame): DataFrame en el que se realizarán las modificaciones.
    lista_col (list): Lista de nombres de columnas en las que se reemplazarán las comas y se convertirá el tipo de dato.

    Retorno:
    pd.DataFrame: DataFrame con las columnas especificadas modificadas.
    """
    for col in lista_col:
        df[col]=df[col].str.replace(',', '.')
        df[col]=df[col].apply(lambda x: float(x))


def formato_fecha(df):
    """
    Convierte las fechas de formato texto a tipo datetime con un formato específico.

    La función reemplaza los nombres de los meses en español por su correspondiente valor numérico 
    y luego convierte la columna 'Date' de tipo texto a un objeto datetime con el formato '%d-%m-%Y'.

    Parámetros:
    df (pd.DataFrame): DataFrame que contiene la columna 'Date' con las fechas en formato texto.

    Retorno:
    pd.DataFrame: DataFrame con la columna 'Date' convertida al tipo datetime.
    """

    meses = {
    'enero': '01',
    'febrero': '02',
    'marzo': '03',
    'abril': '04',
    'mayo': '05',
    'junio': '06',
    'julio': '07',
    'agosto': '08',
    'septiembre': '09',
    'octubre': '10',
    'noviembre': '11',
    'diciembre': '12'
}
    df.replace({'Date': meses}, regex=True, inplace=True)

    df['Date']= pd.to_datetime(df['Date'], format='%d-%m-%Y') 



def mapeo_bool (df, columns, mapping_dict):
    """
    Realiza un mapeo de valores en columnas especificadas utilizando un diccionario de mapeo.

    Parámetros:
    df (pd.DataFrame): DataFrame en el que se realizará el mapeo.
    columns (list): Lista de nombres de las columnas a las que se les aplicará el mapeo.
    mapping_dict (dict): Diccionario que contiene el mapeo de valores, donde las claves son los valores originales 
                         y los valores son los nuevos valores.

    Retorno:
    pd.DataFrame: DataFrame con las columnas mapeadas según el diccionario proporcionado.
    """
  
    for column in columns:
        if column in df.columns:
            df[column] = df[column].map(mapping_dict)













