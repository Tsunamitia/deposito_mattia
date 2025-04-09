#esercizio 1 gestione libreria 

print("Benvenuto nella libreria!")
print("In questo programma puoi aggiungere, rimuovere e cercare libri nel catalogo.")
print("Iniziamo con la creazione di un libro.")
# Definizione della classe Libro
# La classe Libro rappresenta un libro con titolo, autore e ISBN.
# La classe contiene un metodo per stampare le informazioni del libro.
class Libro:
    titolo = ""
    autore = ""
    isbn = ""
    def __init__(self, titolo, autore, isbn ):
        self.titolo = titolo
        self.autore = autore
        self.isbn =isbn
    def stampa_info(self):
        print("Titolo:", self.titolo,"Autore: ", self.autore,"ISBN: ", self.isbn)

# Definizione della classe Libreria
# La classe Libreria rappresenta una libreria con un catalogo di libri.
# La classe contiene metodi per aggiungere, rimuovere, cercare e visualizzare i libri nel catalogo.
# La classe Libreria utilizza la classe Libro per gestire i libri.
# La classe Libreria ha un attributo catalogo che è una lista di libri.
# La classe Libreria ha metodi per aggiungere, rimuovere, cercare e visualizzare i libri nel catalogo.
class Libreria:
 
    # La classe Libreria ha un attributo catalogo che è una lista di libri.
    def __init__(self):
        self.catalogo = []
    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        print("Libro aggiunto al catalogo")
    def rimuovi_libro(self, libro):
        if libro in self.catalogo:
            self.catalogo.remove(libro)
            print("Libro rimosso dal catalogo")
        else:
            print("Libro non trovato nel catalogo")
    def visualizza_catalogo(self):
        if len(self.catalogo) == 0:
            print("Catalogo vuoto")
        else:
            for libro in self.catalogo:
                libro.stampa_info()
    def cerca_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():  # confronto case-insensitiv
                print("Libro trovato:")
                

    
  
libreria=Libreria()

# Funzione per mostrare il menu e gestire le opzioni
# La funzione mostra un menu con le opzioni per aggiungere, rimuovere, cercare e visualizzare i libri nel catalogo.
def apertura_menu(menu): 
        while True:
            print("1. Aggiungi libro")
            print("2. Rimuovi libro")
            print("3. Cerca libro")
            print("4. Mostra catalogo")
            print("5. Esci")
            libro_1=Libro(input("Inserisci il titolo del libro: "), input("Inserisci l'autore del libro: "), int(input("Inserisci l'ISBN del libro: ")))
            scelta = int(input("Scegli un'opzione: "))
            if scelta < 1 or scelta > 5:
                print("Opzione non valida. Riprova.")
                continue
            if scelta == 5:
                print("Arrivederci!")
                break
            elif scelta == 1:
                # Aggiungi libro
                libreria.aggiungi_libro(libro_1)
                print(libro_1.stampa_info())
            elif scelta == 2:
                isbn = int(input("Inserisci l'ISBN del libro da rimuovere: "))
                if isbn == libro_1.isbn:
                    libreria.rimuovi_libro(libro_1)
                    print("Libro rimosso con successo.")
                else:
                    print("Libro non trovato.")
            elif scelta == 3:
                while True: 
                    titolo = input("Inserisci il titolo del libro da cercare: ")
                    if titolo == libro_1.titolo:
                        libreria.cerca_libro(libro_1.titolo)
                        print(libro_1.stampa_info())
                        break
                    elif titolo != libro_1.titolo:
                        print("Libro non trovato, vuoi riprovare? (s/n)")
                        risposta = input()
                        if risposta.lower() == 's':
                            continue
                        elif risposta.lower() == 'n':
                            print("ok!")
                            break
            elif scelta == 4:
                libreria.visualizza_catalogo()
                print("Catalogo visualizzato con successo.")
            

# Inizializza la libreria e mostra il menu
print(apertura_menu(libreria))
    
    
    


