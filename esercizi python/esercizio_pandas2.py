import pandas as pd
import numpy as np  

data = {
    'Prodotto': [
        'Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch',
        'Monitor', 'Tastiera', 'Mouse', 'Stampante', 'Router Wi-Fi',
        'Fotocamera', 'Speaker', 'Hard Disk', 'Power Bank'
    ],
    'Quantità': [12, 30, 20, 50, 25, 18, 40, 60, 10, 35, 15, 45, 22, 55],
    'Prezzo Unitario': [1000, 800, 500, 150, 200, 300, 80, 50, 500, 120, 
                        600, 200, 100, 30],
    'Città': [
        'Milano', 'Roma', 'Napoli', 'Torino', 'Firenze',
        'Bologna', 'Venezia', 'Genova', 'Palermo', 'Bari',
        'Verona', 'Catania', 'Trieste', 'Perugia'
    ]
}

df=pd.DataFrame(data)

df["Totale vendite"]= df["Quantità"] * df["Prezzo Unitario"]

print(df)
print("\n")

#Raggruppare i dati per Prodotto e calcolare il totale delle vendite perciascun prodotto.
dfprod = df.groupby('Prodotto')['Totale vendite'].sum()
print(dfprod)
print("\n")


#il prodotto con il massimo delle vendite
print("Il prodotto maggiormente venduto è: ")
dfprodottomaxven=df.groupby('Prodotto')['Quantità'].sum().idxmax()
print(dfprodottomaxven)
print("\n")
#il prodotto con il massimo delle vendite per ogni città
print("Il prodotto con il massimo delle vendite per ogni città è:")
dfprodottomaxven=df.groupby(['Città', 'Prodotto'])['Quantità'].sum()
print(dfprodottomaxven)
print("\n")
#la citta che hail maggior numero di vendite
print("La città con il maggior numero di vendite è:")
dfprodottomaxvencitta=df.groupby('Città')['Quantità'].sum().idxmax()
print(dfprodottomaxvencitta)
print("\n")
#totale delle vendite > 10000 con la creazione di un nuovo dataframe
df['Totale vendite'] = df['Quantità'] * df['Prezzo Unitario']
#creo una nuova colonna 'Totale vendite' che è il prodotto tra 'Quantità' e 'Prezzo Unitario'
data2=df[df['Totale vendite']> 10000] #creo un nuovo dataframe 'data2' che contiene solo le righe in cui 'Totale vendite' è maggiore di 10000--> per farlo prendo il df originale e lo filtro per la colonna totale vendite df['Totale vendite'] che deve essere maggiore di 10000
ven10000=pd.DataFrame(data2)
print("Le vendite totali superiori a 10000 sono:")
print(ven10000)
print("\n")

#colonna totale vendite in ordcine decrescente
df.sort_values(by='Totale vendite', ascending=False, inplace=True) #utilizzo sort_values per ordinare i dati imposto ascending=False per avere i dati in ordine decrescente se fosse True avrei avuto i dati in ordine crescente,inplace=True per modificare il dataframe originale.
print("Le vendite totali in ordine decrescente sono:")
print(df)
print("\n")