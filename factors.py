n = int(input("Input an int: ")) # Do not change this line
counter=n

# Fill in the missing code below
while counter>0:
    if n%counter==0:
        print(int(n/counter))
    counter-=1
