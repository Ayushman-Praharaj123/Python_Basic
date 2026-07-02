arr=[5,5,8,8,99,40,90,8,8,9,9,2,3]

target = int(input("Enter your num:"))

count =0

for num in arr:
    if num ==target:
        count+=1
        
print(count)