#tipi numerici 
intero= int(input("inserisci numero intero"))               #variabile numerica con numero intero infatti metto int  per indicare la natura del input
virgola= float(input("inserisci numero con la virgola"))    #variabile numerica con numero con la virgola metto float per indicare la natura del input 


#tipi semantici 
stringa= input("Inserisci una parola")                      #variabile semantica non va specificato che tipologia di input è perche verra sempre preso come stringa. 

print(stringa[0])                       #[0] inidica la posizione di partenza, in sto caso sto chiedendo di printare la posizione 0 della parola inserita, cioè la prima lettera.

s="ciao, Mondo"
print(len(s))                           #metodo che mi ristituisce la lunghezza della stringa (s) applicata sulla stringa non modifica
print(s.upper())                        #metodo per convertire la stringa in maiuscolo s.metodo--> modifica la stronga 
print(s.split(','))                       #metodo che consente ogni volta che trova una virgola divide in tre questa 
print(s.replace("Mondo", "Universo"))        # metodo che Rimpiazza la parola mondo con universo

#caratteri= chr(input("inserisci singolo carattere"))        #non contiene metodi 

#valori booleani 
x= False
y= True #ricordarsi di mettere le maiuscole 

print(5>11)
print(5<11)
#operatori logici booleani and,or, not
print(5<11 and 10<20)  #and restituisce true solo se sono vere entrambe                  
print(5<11 or 30<20)   #or restituisce true anche se una delle condizioni è vera  
print(not(4<11))        #not resitiuisce un valore contrario quindi se true resitutisce false e viceversa

#liste insieme di valori tutti in un unico punto.

liste_dati=[1,2,3,4,5,45,30,24]             #valori uguali
lista_dati2=[1,"mirko", True]               #valori diversi
lista_dati3=[]                              # valori non presenti 
liste_dati4= ["marco","mattia","giacomo"]
liste_dati.sort()                           #metodo per riordinare la lista 
liste_dati[0]=20                            #sto sostituendo il primo numero della lista con il valore indicato
print(len(liste_dati))
print(lista_dati2[2])
print(liste_dati)

inserimento=int(input("inserisci un numero"))   #inserisci in una lista vuota dei valori da input dinamico
lista_dati3.append(inserimento) #append metodo per aggiungere 
print(lista_dati3)


