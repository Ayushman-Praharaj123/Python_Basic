arr = [10,20,30,40,50,60]

largest = second = float('inf')

for i in arr:
    if i <largest:
        second = largest
        largest = i
    elif i<second and i != largest:
        second=i
        
print(second)
        