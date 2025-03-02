import pandas as pd
import numpy as np


def calcular_nulos (dataframe):
    """
    Calcula el número total y el porcentaje de valores nulos por cada columna en un DataFrame.

    Parámetros:
    dataframe (pd.DataFrame): El DataFrame sobre el que se calcularán los valores nulos.

    Retorno:
    tupla: Una tupla que contiene dos objetos pandas:
        - El primero es una Serie con el número de valores nulos por columna.
        - El segundo es una Serie con el porcentaje de valores nulos por columna.
    """

    numero_nulos= dataframe.isnull().sum()
    porcentaje_nulos= round((dataframe.isnull().sum()/dataframe.shape[0]) *100,2)
    return numero_nulos, porcentaje_nulos


def analisis_col_cat(dataframe):
    """
    Realiza un análisis descriptivo de las columnas categóricas de un DataFrame.
    Para cada columna categórica, muestra:
    - La cantidad de valores únicos.
    - La distribución de frecuencias normalizada (porcentaje).
    - Un resumen estadístico de la columna.

    Parámetros:
    dataframe (pd.DataFrame): El DataFrame que contiene las columnas categóricas a analizar.

    Retorno:
    None: Imprime los resultados del análisis.
    """

    col_cat=dataframe.select_dtypes(include='O').columns 

    if len (col_cat) == 0:
        print ('No hay columnas categoricas')

    else:
        for col in col_cat:
            print(f'La distribución de la columna {col.upper()}')
            print(f'Esta columna tiene {len(dataframe[col].unique())} valores únicos')
            display(dataframe[col].value_counts(normalize=True))
            print('--------------------\n Describe')
            display(dataframe[col].describe())
            print('--------------------')


def calcular_solo_col_nul(dataframe, umbral=10):
    """
    Calcula y devuelve las columnas con valores nulos en un DataFrame, separadas por un umbral de porcentaje de nulos.
    - Muestra información sobre las columnas con nulos (tipo de datos, número de nulos y porcentaje de nulos).
    - Separa las columnas con porcentaje de nulos superior al umbral de aquellas que tienen un porcentaje de nulos inferior.

    Parámetros:
    dataframe (pd.DataFrame): El DataFrame sobre el que se realizará el análisis.
    umbral (float): El porcentaje de nulos que se considera alto. Las columnas con un porcentaje de nulos superior a este umbral se consideran de alto porcentaje de nulos.

    Retorno:
    high_null_cols (list): Lista de nombres de columnas con un porcentaje de nulos superior al umbral.
    low_null_cols (list): Lista de nombres de columnas con un porcentaje de nulos inferior o igual al umbral.
    """

    columns_with_nulls= dataframe.columns[dataframe.isnull().any()]

    null_columns_info= pd.DataFrame(
        {'Column': columns_with_nulls,
         'Datatype': [dataframe[col].dtype for col in columns_with_nulls],
         'NullCount': [dataframe[col].isnull().sum() for col in columns_with_nulls],
         'Null%': [((dataframe[col].isnull().sum()/ dataframe.shape[0])*100) for col in columns_with_nulls]}
         )

    display(null_columns_info)
    high_null_cols = null_columns_info[null_columns_info['Null%'] > umbral]['Column'].tolist()
    low_null_cols = null_columns_info[null_columns_info['Null%'] <= umbral]['Column'].tolist()
    return high_null_cols, low_null_cols


def imputar_moda(df):
    """
    Rellena los valores nulos de un DataFrame con la moda de cada columna.

    Parámetros:
    df (pd.DataFrame): DataFrame con valores nulos a rellenar.

    Retorna:
    pd.DataFrame: DataFrame con los valores nulos reemplazados por la moda.
    """
    for col in df.columns:
        if df[col].isnull().sum() > 0:  # Verificar si la columna tiene valores nulos
            moda = df[col].mode()[0]  # Obtener la moda de la columna
            df[col] = df[col].fillna(moda)  # Imputar la moda


def contar_outliers(df):
    """
    Cuenta los outliers en cada columna numérica de un DataFrame usando el método del rango intercuartílico (IQR).

    - Calcula los cuartiles Q1 y Q3 de cada columna numérica.
    - Determina los límites inferior y superior para detectar outliers.
    - Cuenta y muestra el número y porcentaje de outliers por columna.

    Parámetros:
    df (pd.DataFrame): DataFrame a analizar.

    Retorno:
    None (los resultados se muestran y se almacenan en un diccionario).
    """

    numeric_cols = df.select_dtypes(include=['number']).columns
    outlier_counts = {}

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]
        percentage = round(outliers / df.shape[0] * 100, 2)

        outlier_counts[col] = {'count': outliers, 'percentage': percentage}
        print(f'Para la columna {col.upper()} tenemos {outliers} outliers, lo que representa un {percentage}% de los datos.')


def eliminar_outliers(df, columnas):
    """
    Elimina outliers en las columnas numéricas de un DataFrame usando el método IQR,
    reemplazándolos por la mediana de la columna.

    Parámetros:
    df (pd.DataFrame): DataFrame con los datos.
    columnas (list): Lista de nombres de columnas a analizar.

    Retorna:
    pd.DataFrame: DataFrame con los outliers eliminados.
    """
    for col in columnas:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        mediana = df[col].median()
        
        df[col] = np.where((df[col] < limite_inferior) | (df[col] > limite_superior), mediana, df[col])
    