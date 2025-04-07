#primo esercizio

print("Benvenuto, segui le istruzioni a schermo per vincere il gioco") #incipit del game 
numero=int(input("inserisci un numero maggiore di 10:"))
if numero > 10:
    print("corretto,livello successivo")
    numero2=int(input("inserisci un numero minore di 100:"))
    if numero2 <100: 
        print("corretto, ultimo livello")
        numero3=int(input("inserisci un numero compreso nell'intervallo 10-100:"))
        if numero3 == 50: 
            print("complimenti hai  vinto.")
        else:
         print("ritenta sarai piu fortuanto :)")



#secondo esercizio
# Lista di esempio
elementi = ["mela", "banana", "kiwi"]

# Menu
print("MENU")
print("1. Aggiungi elemento")
print("2. Visualizza elementi")
print("3. Modifica elemento")
print("4. Rimuovi elemento")

# Input scelta
scelta = input("Scegli un'opzione (1-4): ")

# Aggiungi
if scelta == "1":
    print("lista attuale",elementi[0],elementi[1],elementi[2])
    nuovo = input("Inserisci l'elemento da aggiungere: ")
    elementi.append(nuovo)
    print("Elemento aggiunto.")
    print("lista aggiornata", elementi )
# Visualizza
elif scelta == "2":
    print("lista attuale:",elementi[0],elementi[1],elementi[2])
    
        # Puoi continuare con altri if se la lista può essere più lunga

# Modifica
elif scelta == "3":
    print("lista attuale",elementi[0],elementi[1],elementi[2])

    indice = input("Quale numero vuoi modificare? (1, 2, 3): ")
    if indice == "1":
        nuovo_valore = input("Nuovo valore: ")
        elementi[0] = nuovo_valore
    elif indice == "2" and len(elementi) > 1:
        nuovo_valore = input("Nuovo valore: ")
        elementi[1] = nuovo_valore
    elif indice == "3" and len(elementi) > 2:
        nuovo_valore = input("Nuovo valore: ")
        elementi[2] = nuovo_valore
    print("lista aggiornata", elementi )

# Rimuovi
elif scelta == "4":
    print("lista attuale",elementi[0],elementi[1],elementi[2])
    indice = input("Quale numero vuoi rimuovere? (mela, banana, kiwi): ")
    if indice == "mela":
        elementi.remove("mela")
    elif indice == "banana":
        elementi.remove("banana")
    elif indice == "kiwi":
        elementi.remove("kiwi")

    print("lista aggiornata",elementi)
else:
        print("Indice non valido.")



#esercizio 3 

id=0 
x = True #--> entra per forza in quanto true 
#ciclo 
while x:
 nome=""
 password=""
#registrazione
 nome= input("inserisci tuo nickname:")
 password= input("inserisci la tua password:")
 id +=1
#login 
 if nome == "" or password == "":
        print("non hai valorizzato il campo")
 else: 
    nome_inserito= input("inserisci tuo nickname:")
    password_inserito= input("inserisci la tua password:")

    if nome_inserito==nome and password_inserito==password:
     print("sei loggato")
     x=False
    
    else: 
     print("Password o nickname errati")



        
