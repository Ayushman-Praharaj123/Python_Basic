arr =[10,50,80,20,58,90,22,56]

target = int(input("Enter your number:"))
found = False
for num in arr:
    if num==target:
        found=True
        break
if found:
    print("Found")
else:
    print("Not found")
