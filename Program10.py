n= int(input("Enter your number:"))

largest =0

while n>0:
    digit = n%10
    
    if digit>largest:
        largest=digit
    n//=10
print(largest)