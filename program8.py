n= int(input("Enter your number:"))

reverse = 0

while n>0:
    digit=n%10#gives the last digit of the number 4567 will be 7
    reverse = reverse*10 +digit
    n//=10#removes the last digit every time in a loop 4567 will be 456

print(reverse)
    