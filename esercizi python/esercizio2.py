#esercizio numero 2

for i in range(5): #faccio ripartire il ciclo 5 volte
 numero_pari=int(input("inserisci per 5 volte un numero pari")) #chiedo di inserire un numero pari
 if numero_pari % 2 == 0: #controllo se il numero è pari
  print("il numero è pari")
 else: #controllo se il numero è dispari
     print("il numero non è pari")
     
#correzzione 
# Lista per salvare i numeri pari trovati
numeri_pari = []

# Ciclo finché non abbiamo trovato 5 numeri pari
while len(numeri_pari) < 5:
    numero = int(input("Inserisci un numero: "))
    
    if numero % 2 == 0:
        print("Il numero è pari")
        numeri_pari.append(numero)
    else:
        print("Il numero non è pari")

# Alla fine stampa i numeri pari raccolti
print("Hai inserito 5 numeri pari:", numeri_pari)
