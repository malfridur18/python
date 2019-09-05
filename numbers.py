#numbers.py
for i in range(10,100): #range(10-100) því allar tveggja stafa tölur eru þar
    fyrri_tala=i//10 #finnum fyrri stafinn
    seinni_tala=i%10 #finnum seinni stafinn
    summa=fyrri_tala+seinni_tala #leggjum saman fyrri og seinni
    summa2=summa**2 #summan í öðru veldi
    if summa2==i: #ef summan er jöfn tölunni
        print(i)

for j in range(1,100): #allar jákvæðar tölur minni en 100
    counter=0 #teljari til að telja deilana
    for k in range(1,100): #tölurnar sem er deilt með
        if j%k==0: #ef að talan er deilir
            counter+=1
    if counter==10: #ef að talan er með 10 deila
        print(j)

