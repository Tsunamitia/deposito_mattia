#controllo se il numero è pari o dispari esercizio 1
numero=(int(input("inserisci un numero: "))) #input dell'utente
#controllo se il numero è pari o dispari
if numero%2==0:
    #se il numero è pari
    print("il numero è pari")
#se il numero è dispari
else:
    print("il numero è dispari")

#esercizio 2
x=True
while x:
    #input dell'utente
    numero=(int(input("inserisci un numero: ")))
    #conto alla rovescia:
    for i in range(numero,-1,-1):
        print(i)

    #chiedo all'utente se vuole continuare
    risposta=input("vuoi continuare? (si/no)").lower()
#controllo se l'utente vuole continuare
    if risposta=="no":
        #se l'utente non vuole continuare
        x=False
