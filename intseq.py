summa=0
x=1
maxint=0
slettar=0
odda=0
while x>0:
    x=int(input('Enter an integer: '))
    summa=summa+x
    print('Culmulative total: ',summa)
    if x>maxint:
        maxint=x
    if x%2==0 and not x==0:
        slettar=slettar+1
    if x%2==1:
        odda=odda+1
    if x<=0:
        print('Largest number: ',maxint)
        print('Count of even numbers: ',slettar)
        print('Count of odd numbers: ',odda)
        
    
