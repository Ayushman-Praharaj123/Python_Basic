n = int (input("Enter your number:"))
total = 0

while n>0:
    digit =n%10 #gives the last digit of the number 4567 will be 7
    total +=digit #stores the last digit by adding pervious one 
    n//=10#removes the last digit every time in a loop 4567 will be 456

print("sum:",total)