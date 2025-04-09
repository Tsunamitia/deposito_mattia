#esercizio 1 
class Punto:
    def __init__ (self, x, y):
        self.x =x
        self.y =y 
    
    def muovi(self, dx, dy):
        if dx > 0 and dy > 0 :
            self.x += dx
            self.y += dy
            return (self.x, self.y) #restituisce le nuove coordinate del punto
        else:
              print("Le coordinate non possono essere negative.")
         
    
    def distanza(self, px, py):
        self.px=0
        self.py=0
        return ((self.x - px)**2 + (self.y - py)**2)**0.5
     
while True:
    scelta= input("Vuoi inserire le coordinate di un punto? (s/n): ")
    if scelta.lower() == 's':
        x= int(input("Inserisci la coordinata x: "))
        y= int(input("Inserisci la coordinata y: "))
        p= Punto(x, y)
        print(f"Le coordinate del punto sono: ({p.x}, {p.y})")
    scelta= input("Vuoi muovere il punto? (s/n): ")
    if scelta.lower() == 's':
        dx= int(input("Inserisci la distanza da muovere in x: "))
        dy= int(input("Inserisci la distanza da muovere in y: "))
        print(f"Le nuove coordinate del punto sono: {p.muovi(dx, dy)}")
    elif scelta.lower() == 'n':
        print("Operazione annullata.")
        break
    scelta= input("Vuoi calcolare la distanza dall'origine? (s/n): ")
    if scelta.lower() == 's':
        px= 0
        py= 0
        print(f"La distanza dall'origine è: {p.distanza(px, py)}")
    elif scelta.lower() == 'n':
        print("Operazione annullata.")
        break
    scelta= input("Vuoi continuare? (s/n): ")
    if scelta.lower() != 'n':
        break
        