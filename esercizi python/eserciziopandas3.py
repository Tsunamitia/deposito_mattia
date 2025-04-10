import pandas as pd
import numpy as np

 

data1 = {
    "data": np.random.randint(1, 31, 30),
    "citta": np.random.choice(["Roma", "Milano", "Torino",np.nan], 30),
    "Prodotto": np.random.choice(["Laptop", "Smartphone", "Tablet",np.nan], 30),
    "vendite": np.random.randint(1, 100, 30)}

#creazione di una tabella pivot 
df = pd.DataFrame(data1)
print(df)
print("\n")
df_unique = df.drop_duplicates()
print(df_unique)
print("\n")
df_cleaned=df_unique.dropna()
print(df_cleaned)
print("\n")
print(df_unique)
print("\n")
pivot_df=df_unique.pivot_table(values='vendite', index='Prodotto', columns='citta', aggfunc='mean')

print(pivot_df)
print("\n")

venditetotprod=df_cleaned.groupby("Prodotto")["vendite"].sum()

print(venditetotprod)