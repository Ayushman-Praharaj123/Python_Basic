arr =[1,5,3,8,9,5,66,5]

target = int(input("Enter your num:"))

for i in range (len(arr)):
    if arr[i] == target:
        print("First occurance:",i)
        break
    else:
        print("Not found")