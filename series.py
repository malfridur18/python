tala=int(input('sladu inn tolu:'))
bil=int(input('bilid:'))
hamark=100
summa=0
while summa<hamark:
    print(tala,end=' ')
    summa=summa+tala
    tala=tala+bil
print('')
print('summan er',summa)