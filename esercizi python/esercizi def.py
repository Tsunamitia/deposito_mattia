# In questo esercizio, il giocatore deve indovinare un numero casuale tra 1 e 100.
# Se il giocatore indovina, il programma stampa "Hai indovinato!" e termina.
# Se il giocatore sbaglia, il programma stampa "Hai sbagliato, il numero era: " seguito dal numero casuale.
import random
def numero_randomico(): # funzione che restituisce un numero casuale tra 1 e 100
    return random.randint(1, 100)

x=True
valore_randomico=numero_randomico()
print("Benvenuto nel gioco del numero casuale!")
while x: # ciclo che continua finché il giocatore non indovina il numero
    
    numero_giocatore=int(input("Inserisci un numero compreso tra 1 e 100: "))
    if numero_giocatore== valore_randomico: # se il numero del giocatore è uguale al numero casuale
        print("Hai indovinato!")
        x=False
    elif numero_giocatore < valore_randomico: # il numero del giocatore è più alto
        print("il numero è piu alto, vuoi continuare a giocare?")
        risposta=input("si o no? ").lower()
        if risposta == "si":
            continue
        else:
            print("Hai sbagliato, il numero era:", valore_randomico)
            x=False
    elif numero_giocatore > valore_randomico: # il numero del giocatore è più basso
        print("il numero è piu basso, vuoi continuare a giocare?") 
        risposta2=input("si o no? ").lower()   
        if risposta2 == "si":
            continue
        else: 
            print("Hai sbagliato, il numero era:", valore_randomico)
            x=False
    


#esercizio 2 
# Sequenza di Fibonacci fino ad un numero n
def fibonacci(n):
    fib = [0, 1]
    while fib[-1] <= n : # continua a calcolare i numeri di Fibonacci finché l'ultimo numero è minore di n
     fib.append(fib[-1] + fib[-2]) # calcola il numero di Fibonacci successivo
    return fib[:-1] if fib[-1] > n else fib # restituisce la lista dei numeri di Fibonacci fino a n
# Esempio di utilizzo   
n = int(input("Inserisci un numero: "))
print(fibonacci(n))
