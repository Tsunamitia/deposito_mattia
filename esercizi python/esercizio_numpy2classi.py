import numpy as np
# es2
#creo una array di 50 elementi equidistanti tra 0 e 10
class Myarray:
    def __init__(self):
        self.arr =[]
    def aggiunta (self,vi,vf,numero):
        self.vi=vi
        self.vf=vf
        self.numero=numero
        self.arr = np.linspace(vi, vf, numero)
    
Array1=Myarray()

Array1.aggiunta(0,10,50)
\
print("Array1: ", Array1.arr)

#creo un array di 50 numeri casuali
class Myarray2:
    def __init__(self):
        self.arr = []
    def randomizzazione(self,valore):
        self.valore=valore
        self.arr=np.random.rand(valore)
Array2=Myarray2()
Array2.randomizzazione(50)
#stampo i risultati
print("Array2: ", Array2.arr)

#somma dei due array
arr5=Array1.arr + Array2.arr
#stampo i risultati
print(arr5)
#somma dei numeri maggiori di 5
arr6=arr5[arr5>5]
somma6=np.sum(arr6)

#for i in range(50):
   # if arr5[i] > 5:
        #np.sum(arr5[i])
#print("Somma: ", np.sum(arr5))
    

    
