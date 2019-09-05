m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line
gcd=0
if m<n:
    for i in range(1,m):
        if m%i==0 and n%i==0:
            gcd=i
    print(gcd)
    

if n<m:
    for i in range(1,n):
        if m%i==0 and n%i==0:
            gcd=i
    print(gcd)
