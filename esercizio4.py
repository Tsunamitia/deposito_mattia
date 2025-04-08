# Scrivi un programma che calcoli il quadrato di ogni numero in una lista di numeri.
numeri=[2,3,4,4,5,6,7,8,9] #lista di numeri
# Il programma calcola il quadrato di ogni numero nella lista e lo stampa.
for i in numeri:
        print(i**2)


# Esercizio 4
numeri=[] #lista di numeri
x=True 
while len(numeri) < 4 : #finchè la lista non ha 4 numeri
    numero=int(input("inserisci un numero maggiore di 0:")) #chiedi all'utente di inserire un numero
    if numero== 0: #se il numero è 0
        x=False #ferma il ciclo
    else:
        numeri.append(numero) #aggiungi il numero alla lista
print(numeri) #stampa la lista di numeri
for numero in numeri:  # per ogni numero nella lista
    print(max(numeri))  # stampa il numero massimo
    break  # interrompi il ciclo dopo aver stampato il massimo
if numeri == []: #se la lista è vuota
    print("la lista è vuota") #stampa che la lista è vuota
else:
    print(len(numeri)) #altrimenti stampa il numero massimo
    print(numeri) #stampa il numero minimo