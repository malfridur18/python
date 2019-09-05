first=int(input('First : '))
step=int(input('step: '))
summa=0
while summa<100:
    print(first,end=' ')
    summa=summa+first
    first=first+step
print()
print('Sum of series: ',summa)
    
