n = int(input("Input a natural number: ")) # Do not change this line
counter=2
# Fill in the missing code below
prime=0
# Do not changes the lines below
if n==2:
    prime=1
else:
    while n%counter!=0:
        counter+=1
        prime=1
    


if prime:
    print("Prime")
    print(prime)
else:
    print("Not prime")
    print(prime)
