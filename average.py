fjoldi=int(input('hversu margar tolur:'))
summa=0
minint=1000
for i in range(1,fjoldi+1):
    tala=int(input('Tala:'))
    while tala<minint:
        minint=tala
    else:
        summa=summa+tala
aver=int((summa-minint)/(fjoldi-1))
print('The average is: ', aver)
print(summa-minint)
print(minint)