#es1 con extra 
import numpy as np
#creo una classe di un array 
class MyArray:
    def __init__(self):
        self.arr = []
    def creazione(self,vi,vf,n):
        self.vi=vi
        self.vf=vf
        self.n=n
        self.arr = np.linspace(vi, vf, n)
    def cambio_forma(self,rigan,colonnan):
        self.rigan=rigan
        self.colonnan=colonnan
        self.arr = self.arr.reshape(rigan,colonnan)
    #definisco un metodo per calcolare la somma degli elementi dell'array
    def sommatot(self):
        self.somma=np.sum(self.arr)
        return self.somma
    
#creo un array di 12 elementi equidistanti tra 0 e 1
Array = MyArray()
Array.creazione(0,1,12)
Array.cambio_forma(3,4)

print("Array: ",Array.arr)



#creo una classe di un array 2d
class MyArray2:
    def __init__(self):
        self.arr = []
    def creazione_randomica(self,rig,col):
        self.rig=rig
        self.col=col
        self.arr = np.random.rand(rig,col)
    def sommatot1(self):
        self.somma=np.sum(self.arr)
        return self.somma
    
Array2 = MyArray2()
Array2.creazione_randomica(3,4)

print("Array2: ",Array2.arr)
#somma di entrmabe le matrici

somma1=Array.sommatot()
s2=Array2.sommatot1()
#stampo i risultati
print("somma Array3:",somma1)
print("somma Array2:",s2)