import os 
import random
os.system('cls')


a= list(range(1,100))
angka = random.sample(a,k=10)

def quickSort(arr):
    if len(arr) <=1 :
        return arr
	
    elif len(arr)> 1:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]    
	
        right = [i for i in arr[1:] if i >= pivot]
        
        return quickSort(left) + [pivot] + quickSort(right)


print(f"Data sebelum di urutkan {angka}")

hasil = quickSort(angka)

print(f"Data setelah diurutkan {hasil}")