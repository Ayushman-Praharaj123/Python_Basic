n = int (input("Enter your number:"))

if n<2:
    print("Not prime")
else:
    is_prime =True
    
    for i in range(2,int(n**0.5)+1,):
        if i==0:
            is_prime=False
            break
if is_prime:
    print("Prime")
else:
    print("Not a prime")
        