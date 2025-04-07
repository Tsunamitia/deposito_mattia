#controllo del flusso RICORDARSI DI METTERE I DUE PUNTI 
#blocco delle condizione 
numero=int(input("inserisci un numero")) 
if numero >= 0:      #IF viene printato se la condizione è true è uno per blocco ed è all'inizio e posso annidarli                      
    print("il numero è positivo")
    if numero == 100: #if annidato se non rispetto la prima condizione non posso entrare nel secondo if; nel caso si verifichino entrambe le casistiche printa entrambe
        print("woow")
elif numero < 0 :  # condizione intermedia letta solo se il pirmo if è false
    print("il numero è negativo")
else:              #Else viene letto solo se le latre condizione sono false IMPOSSIBILE CHE VENGANO PRINTATE INSIEME 
    print("Blocco Else")




#ciclo booleano 

controllore= True 
while controllore: #continua a printare finche la variabile controllore diventa False 
    print(1)
    controllore=False 