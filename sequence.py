n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter=0
x1=1
x2=2
x3=3
print(x1,x2,x3)
for i in range(4,n):
    counter=x1+x2+x3
    x1=x2
    x2=x3
    x3=counter
    print(counter,end=', ')

