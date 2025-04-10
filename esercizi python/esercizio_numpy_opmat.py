import numpy as np

#es1 senza extra

arr = np.linspace(0,1,12)
arr1=arr.reshape(3,4)
arr2 = np.random.rand(3,4)

#somma di entrmabe le matrici
somma1 = np.sum(arr1)
somma2 = np.sum(arr2)

print("somma arr1: ", somma1)
print("somma arr2: ", somma2)   



#es2
#creo una array di 50 elementi equidistanti tra 0 e 10
class Myarray:
    def __init__(self,lista):
        self.lista = lista
    def arr(self):
        return np.linspace(0,10,50)
    
Array1=Myarray(arr)

print("Array1: ", Array1.arr())
        
    

    
#creo una array di 50 elementi equidistanti tra 0 e 10
arr3=np.linspace(0,10,50)
print(arr3)
#creo un array di 50 numeri casuali
arr4=np.random.rand(50)
print(arr4)
#somma dei due array
arr5=arr3+arr4
#stampo i risultati
print(arr5)