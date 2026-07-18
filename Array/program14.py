arr = [0,2,0,5,0,2,0]

position = 0

for i in range(len(arr)):
    if arr[i] !=0:
        arr[position]=arr[i]
        position +=1
        
while position < len(arr):
    arr[position] =0
    position +=1
    
print(arr)