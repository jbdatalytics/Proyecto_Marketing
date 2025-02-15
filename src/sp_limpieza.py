import pandas as pd


def eda_preliminar(df):

    
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

    for col in df.select_dtypes(include='O'). columns:    # cambio a minúscula todo el contenido del dataframe
        df[col]=   df[col].str.lower()


def comas (df,lista_col):
    for col in lista_col:
        df[col]=df[col].str.replace(',', '.')
        df[col]=df[col].apply(lambda x: float(x))


def formato_fecha(df):

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
  
    for column in columns:
        if column in df.columns:
            df[column] = df[column].map(mapping_dict)













