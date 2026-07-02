arr = [5,2,6,8,9,7,5,8,9,9,5]

target = int(input("Enter your number:"))
last = -1

for i in range(len(arr)):
    if arr[i] == target:
        last=i
    
print("The last occurance is:",last)