import pandas as pd

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
print("5. Identificare:")
duplicati = tabella.duplicated()
if duplicati.any():
    print("Ci sono duplicati")
    print("cancello i duplicati")
    tabella = tabella.drop_duplicates()
    print("Duplicati rimossi")
else:
    print("Non ci sono duplicati")
print("\n")
#6 sostituire i valori mancanti con la mediana della colonna
print("6. Sostituire i valori mancanti con la mediana della colonna:")
