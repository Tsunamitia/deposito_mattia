import pandas as pd
import numpy as np
#Importo di un dataframe 
file_path = 'dataset_persone_30.csv'
# Leggi il file CSV
df = pd.read_csv(file_path)

tabella=pd.DataFrame(df)

# 1. Visualizza le prime 5 righe del DataFrame
print("1. Prime 5 righe del DataFrame:")
print(tabella.head(5))
print("\n")
# 2. Visualizza le ultime 5 righe del DataFrame
print("2. Ultime 5 righe del DataFrame:")
print(tabella.tail(5))
print("\n")
#3 visualizzare i tipo di dati delle colonne
print("3. Tipo di dati delle colonne:")
print(tabella.dtypes)
print("\n")
#4 Calcoalre media,medianam, deviazione standard delle colonne numeriche
print("4. Statistiche descrittive:")
print(tabella.describe())

#5 identificare e rimuovere i duplicati
print("5. rimozione dei duplicati:")
tabella=tabella.drop_duplicates()
print("duplicati rimossi")
print("\n")

#6 sostituire i valori mancanti con la mediana della colonna
print("6. Sostituire i valori mancanti con la mediana della colonna:")
tabella["Età"].fillna(tabella["Età"].median(), inplace=True)
tabella["Salario"].fillna(tabella["Salario"].median(), inplace=True)
print("Valori mancanti sostituiti")
print("\n")

#7 aggiungere una nuova colonna "categoria età" che classifica le persone in base alla loro età
print("7. Aggiungere una nuova colonna 'categoria età':")
def categoria_eta(eta):

    if eta < 18:
        return 'Minorenne'
    elif 18 <= eta < 65:
        return 'Adulto'
    else:
        return 'Anziano'

#creo una nuova colonna e applico la funzione
tabella['categoria_eta'] = tabella['Età'].apply(categoria_eta)

print("Colonna 'categoria eta' aggiunta")
print(tabella[['Età', 'categoria_eta']].head(10))

#salvo il file
tabella.to_csv('dataset_persone_30_modificato.csv', index=False)
print("\n")
