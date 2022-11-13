import pandas as pd
import re
import numpy as np

df = pd.read_csv('disney_plus_titles.csv', sep=',')

def extract():
    df = pd.read_csv('disney_plus_titles.csv')
    return df

def transform(df, entrada):
    print('Here are the results for films under', entrada, ':\n') 
    regex = re.compile(entrada, re.IGNORECASE)
    recomendaciones = []
    for i in range(len(df)):
        fila = df.iloc[i]
        if re.search(regex, fila['listed_in']):
            titulo = fila['title']
            recomendaciones.append(titulo)
    return recomendaciones

def load(df, entrada):
    recomendaciones = transform(df, entrada)
    for i in range(len(recomendaciones)):
        print(recomendaciones[i])

if __name__ == '__main__':
    df_cargado = extract()
    entrada = input('What genre would you like to watch?: ')
    load(df_cargado, entrada)