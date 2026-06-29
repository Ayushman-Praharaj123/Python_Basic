#Print multiplication table of N
n = int (input("enter your number you want to print table:"))
for i in range(1,11):
    print(f"{n}x{i}=",i*n)