
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import math

def subplot_col_cat(dataframe):
    """
    Crea subgráficos de barras para cada columna categórica del DataFrame.

    Esta función selecciona las columnas de tipo 'object' o 'category' del DataFrame y genera un gráfico 
    de barras para cada una, mostrando la frecuencia de los valores. Los subgráficos se organizan de manera 
    automática en una cuadrícula según la cantidad de columnas categóricas.

    Parámetros:
    dataframe (pd.DataFrame): DataFrame con las columnas categóricas a graficar.

    Retorno:
    None: La función muestra los gráficos de barras, pero no retorna ningún valor.
    """
    # seleccionar columnas categóricas
    categorical_cols= dataframe.select_dtypes(include= ['object']).columns

    if len (categorical_cols) == 0:
        print('No hay columnas categóricas en el dataframe')
        return
    
    # configurar el tamaño de la figura  
    num_cols=len(categorical_cols)
    rows = math.ceil(num_cols / 4)
    fig, axes= plt.subplots(rows, 4, figsize=(15, rows * 5))
    axes= axes.flatten()          

    # generar gráficos para cada columna categórica  
    for i, col in enumerate(categorical_cols):
        sns.countplot(data=dataframe, x=col, ax=axes[i], hue=col, palette='tab10', legend=False)
        axes[i].set_title(f'Distribución de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel ('Frecuencia')
        axes[i].tick_params(axis='x', rotation=45)  

  # eliminar ejes sobrantes si hay menos columnas que subplots
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])
        
    plt.tight_layout()
    plt.show()


def subplot_col_num(dataframe,col):
    """
    Crea un conjunto de subgráficos para visualizar la distribución y los valores atípicos de las columnas numéricas.

    La función genera un gráfico de histograma y un boxplot para cada columna numérica especificada en la lista `col`.
    Los histogramas muestran la distribución de los valores, mientras que los boxplots visualizan los valores atípicos.
    Los gráficos se organizan en una cuadrícula con una fila para cada columna numérica.

    Parámetros:
    dataframe (pd.DataFrame): DataFrame que contiene las columnas numéricas a analizar.
    col (list): Lista de nombres de las columnas numéricas para las que se generarán los gráficos.

    Retorno:
    None: La función genera los gráficos y los muestra, pero no retorna ningún valor.
    """

# Creo una sola paleta de gráficos de histogramas y boxplot para un mejor análisis
    num_graphs=len(col)
    rows= (num_graphs + 2) // 2   
    fig, axes= plt.subplots(num_graphs, 2, figsize=(15, rows * 5))     

    for i, col in enumerate(col):
        sns.histplot(data=dataframe, x=col, ax=axes[i,0], bins=200)
        axes[i,0].set_title(f'Distribución de {col}')
        axes[i,0].set_xlabel (col)
        axes[i,0].set_ylabel ('Frecuencia')

        sns.boxplot(data=dataframe, x=col, ax=axes[i,1])
        axes[i,1].set_title(f'Boxplot de {col}')

    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()



def subplot_subs_cat(dataframe):
    """
    Crea un conjunto de subgráficos para visualizar la tasa de suscripción de una variable categórica.

    La función genera tres gráficos de barras, cada uno correspondiente a una variable categórica 
    ('Job', 'Marital', 'Education') que muestra la tasa de suscripción ('Y') en porcentaje. Los gráficos
    presentan cómo varía la tasa de suscripción según las categorías de cada una de estas variables.

    Parámetros:
    dataframe (pd.DataFrame): DataFrame que contiene las variables categóricas y la columna 'Y' (indicador de suscripción).

    Retorno:
    None: La función genera los gráficos y los muestra, pero no retorna ningún valor.
    """

    # Configurar estilo
    sns.set_style("whitegrid")

    # Crear figura con 3 subgráficos en una fila
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Variables categóricas a analizar
    categorical_vars = ['Job', 'Marital', 'Education']

    # Crear gráficos para cada variable categórica
    for i, var in enumerate(categorical_vars):
        # Calcular la tasa de suscripción en porcentaje
        rate_df = dataframe.groupby(var)['Y'].value_counts(normalize=True).unstack() * 100
        rate_df = rate_df.rename(columns={'yes': 'Subscription Rate'})  
        
        # Crear gráfico de barras
        sns.barplot(x=rate_df.index, y=rate_df['Subscription Rate'], hue=rate_df.index, ax=axes[i], palette='viridis', legend=False)
        
        # Configurar título y etiquetas
        axes[i].set_title(f'Subscription Rate by {var.capitalize()}', fontsize=14)
        axes[i].set_ylabel('Subscription Rate (%)')
        axes[i].set_xlabel(var.capitalize())
        axes[i].tick_params(axis='x', rotation=45)  

    # Ajustar diseño
    plt.tight_layout()
    plt.show()


    
def subplot_subs_relationships(df):
    """
    Crea una cuadrícula de subgráficos que muestra la relación entre varias variables y la suscripción ('Y').

    La función genera cuatro gráficos: dos histogramas y dos gráficos de barras, para visualizar la relación 
    entre las variables numéricas y categóricas con la variable de suscripción ('Y'). Los gráficos permiten 
    observar cómo varían las distribuciones y las frecuencias de suscripción según las características de las 
    variables 'Age_iterative', 'Income', 'Kidhome' y 'Teenhome'.

    Parámetros:
    df (pd.DataFrame): DataFrame que contiene las variables 'Age_iterative', 'Income', 'Kidhome', 'Teenhome' y 'Y' (indicador de suscripción).

    Retorno:
    None: La función genera los gráficos y los muestra, pero no retorna ningún valor.
    """
   
    fig, axes = plt.subplots(2, 2, figsize=(20, 14))  

    # Gráfico 1: Distribución de Age_iterative por suscripción
    sns.histplot(data=df, x="Age_iterative", hue="Y", bins=30, kde=True, ax=axes[0, 0], palette="coolwarm", alpha=0.7)
    axes[0, 0].set_title("Subscription by Age")
    axes[0, 0].set_xlabel("Age")
    axes[0, 0].set_ylabel("Frequency")

    # Gráfico 2: Distribución de Income por suscripción
    sns.histplot(data=df, x="Income", hue="Y", bins=30, kde=True, ax=axes[0, 1], palette="coolwarm", alpha=0.7)
    axes[0, 1].set_title("Subscription by Income")
    axes[0, 1].set_xlabel("Income")
    axes[0, 1].set_ylabel("Frequency")

    # Gráfico 3: Relación entre Kidhome e Y
    sns.countplot(x="Kidhome", hue="Y", data=df, ax=axes[1, 0], palette="viridis")
    axes[1, 0].set_title("Subscription by Kidhome")
    axes[1, 0].set_xlabel("Kidhome")
    axes[1, 0].set_ylabel("Count")

    # Gráfico 4: Relación entre Teenhome e Y
    sns.countplot(x="Teenhome", hue="Y", data=df, ax=axes[1, 1], palette="viridis")
    axes[1, 1].set_title("Subscription by Teenhome")
    axes[1, 1].set_xlabel("Teenhome")
    axes[1, 1].set_ylabel("Count")

    # Ajustes finales para mejor visualización
    plt.tight_layout()
    plt.show()


def subplot_contact_and_duration(df):
    """
    Crea una cuadrícula de subgráficos que muestra la tasa de suscripción por método de contacto y por duración de llamada.

    La función genera dos gráficos de barras para visualizar la tasa de suscripción en función de dos variables:
    el método de contacto ('Contact') y la duración de la llamada ('Duration'). Los gráficos permiten comparar 
    la tasa de conversión (suscripción) para diferentes categorías de contacto y duración de llamada.

    Parámetros:
    df (pd.DataFrame): DataFrame que contiene las columnas 'Contact', 'Duration', y 'Y' (indicador de suscripción).

    Retorno:
    None: La función genera los gráficos y los muestra, pero no retorna ningún valor.
    """

    fig, axes = plt.subplots(1, 2, figsize=(18, 6))  # Crear figura con 1 fila y 2 columnas

    # Gráfico 1: Tasa de éxito según el método de contacto 
    contact_counts = df.groupby("Contact", observed=False)["Y"].value_counts(normalize=True).unstack(fill_value=0) * 100  

    # Verificar si "yes" o 1 es la clave correcta
    success_key = "yes" if "yes" in contact_counts.columns else 1 if 1 in contact_counts.columns else None
    if success_key is None:
        print("No se encontraron datos de conversión en la columna 'Y'. Verifica los valores.")
        return

    sns.barplot(x=contact_counts.index, y=contact_counts[success_key], hue=contact_counts.index, 
                ax=axes[0], palette="coolwarm", legend=False)
    
    axes[0].set_title("Subscription Rate by Contact", fontsize=14)
    axes[0].set_ylabel("Subscription Rate (%)")
    axes[0].set_xlabel("Contact Method")
    axes[0].tick_params(axis='x', rotation=45)

    # Agregar etiquetas a las barras
    for p in axes[0].patches:
        axes[0].annotate(f"{p.get_height():.2f}%", 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha='center', va='bottom', fontsize=10)

    # Gráfico 2: Tasa de conversión según la duración de la llamada 
    bins = [0, 60, 180, 300, 600, df["Duration"].max()]  # Intervalos en segundos
    labels = ["<1 min", "1-3 min", "3-5 min", "5-10 min", "10+ min"]
    df["Duration_Category"] = pd.cut(df["Duration"], bins=bins, labels=labels, right=False)

    duration_counts = df.groupby("Duration_Category", observed=False)["Y"].value_counts(normalize=True).unstack(fill_value=0) * 100  

    sns.barplot(x=duration_counts.index, y=duration_counts[success_key], hue=duration_counts.index, 
                ax=axes[1], palette="viridis", legend=False)

    axes[1].set_title("Subscription Rate by Duration", fontsize=14)
    axes[1].set_ylabel("Subscription Rate  (%)")
    axes[1].set_xlabel("Duration Call")
    axes[1].tick_params(axis='x', rotation=45)

    # Agregar etiquetas a las barras
    for p in axes[1].patches:
        axes[1].annotate(f"{p.get_height():.2f}%", 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha='center', va='bottom', fontsize=10)

    # Ajustar diseño
    plt.tight_layout()
    plt.show()



def subplot_subs_by_credit_factors(df):
    """
    Crea una cuadrícula de subgráficos que muestra la tasa de suscripción en función de factores de crédito.

    La función genera tres gráficos de barras que visualizan la tasa de suscripción ('Y') en relación con tres variables:
    el historial de crédito ('Default'), la posesión de vivienda ('Housing') y si se tiene un préstamo personal ('Loan').
    Cada gráfico presenta la tasa de conversión de suscripción para las diferentes categorías de estas variables.

    Parámetros:
    df (pd.DataFrame): DataFrame que contiene las columnas 'Y', 'Default', 'Housing', y 'Loan'.

    Retorno:
    None: La función genera los gráficos y los muestra, pero no retorna ningún valor.

    La columna 'Y' se mapea a valores numéricos, donde 'yes' se convierte en 1 y 'no' en 0, para calcular la tasa de suscripción por cada categoría de las variables de crédito.
    Las barras de los gráficos se etiquetan con los valores porcentuales correspondientes.
    """
   
    df['Y_numeric'] = df['Y'].map({'yes': 1, 'no': 0})

    default_pct = df.groupby("Default")["Y_numeric"].mean() * 100
    housing_pct = df.groupby("Housing")["Y_numeric"].mean() * 100
    loan_pct = df.groupby("Loan")["Y_numeric"].mean() * 100

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Gráfico 1: Subscription Rate by Default 
    sns.barplot(x=default_pct.index, y=default_pct.values, hue=default_pct.index, palette="coolwarm", legend=False, ax=axes[0])
    axes[0].set_title("Subscription Rate by Default")
    axes[0].set_xlabel("Default History")
    axes[0].set_ylabel("Subscription Rate (%)")

    for index, value in enumerate(default_pct.values):
        axes[0].text(index, value + 0.5, f"{value:.2f}%", ha='center', fontsize=10)

    # Gráfico 2: Subscription Rate by Housing
    sns.barplot(x=housing_pct.index, y=housing_pct.values, hue=housing_pct.index, palette="Blues_r", legend=False, ax=axes[1])
    axes[1].set_title("Subscription Rate by Housing ")
    axes[1].set_xlabel("Mortgage")
    axes[1].set_ylabel("Subscription Rate (%)")

    for index, value in enumerate(housing_pct.values):
        axes[1].text(index, value + 0.5, f"{value:.2f}%", ha='center', fontsize=10)

    # Gráfico 3: Subscription Rate by Loan s
    sns.barplot(x=loan_pct.index, y=loan_pct.values, hue=loan_pct.index, palette="Reds_r", legend=False, ax=axes[2])
    axes[2].set_title("Subscription Rate by Loan")
    axes[2].set_xlabel("Personal Loan")
    axes[2].set_ylabel("Subscription Rate (%)")

    # Add labels on bars
    for index, value in enumerate(loan_pct.values):
        axes[2].text(index, value + 0.5, f"{value:.2f}%", ha='center', fontsize=10)

    # Adjust layout
    plt.tight_layout()
    plt.show()



