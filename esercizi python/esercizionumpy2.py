import numpy as np

arr = np.random.randint(1, 101, (6, 6))
print("Matrice originale:")
print(arr)

# Seleziona il blocco 2x2 in posizione [2:4, 2:4]
arr1 = arr[2:4, 2:4]
print(arr1)

# Scambia le due righe di arr1
arr2 = arr1[[1, 0], :]
print(arr2)
#prendo la diagonale principale
arr3 = np.diag(arr2) #arr3 = arr2[[0, 1],[0,1]] modi uguali per estrarre la diagonale
print(arr3)

if arr2[0, 0] % 3 == 0: #il primo elemento della diagonale è divisibile per 3
    arr2[0, 0] = -1
if arr2[1, 1] % 3 == 0: #il secondo elemento della diagonale è divisibile per 5
    arr2[1, 1] = -1
if arr2[0, 1] % 3 == 0: #il terzo elemento della diagonale è divisibile per 7
    arr2[0, 1] = -1
if arr2[1, 0] % 3 == 0: #il quarto elemento della diagonale è divisibile per 11
    arr2[1, 0] = -1

arr4=arr2

print(arr4)

print(arr,arr1, arr2, arr3, arr4)