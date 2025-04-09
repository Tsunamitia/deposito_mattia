import  numpy as np


#creo un array da 10 a 49
arr=np.arange(10,50)
print(arr)
#verifico il tipo di dato
print("il dato è :",arr.dtype)
#cambio il tipo di dato in float64
arr2=np.array(arr, dtype="float64")
#verifico il tipo di dato
print("il dato è :",arr2.dtype)
#verifico la forma dell'array
print("la forma è :",arr.shape)

#creo un array di 20 numeri casuali tra 10 e 50

arr=np.random.randint(10,51,20)
print(arr)
#prendo i primi 10 valori

arr2=arr[0:10]
print(arr2)

#gli ultimi 5 valori
arr3=arr[16:21]
print(arr3)
#prendo i valori da 0 a 20 con passo 3
arr4=arr[0:21:3]
print(arr4)
#sostituisco i valori da 5 a 10 con 99
arr1=arr
arr[5:10]=99
print(arr1)






