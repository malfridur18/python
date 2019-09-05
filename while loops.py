counter=1
while counter<=18:
    par=int(input(f'Par of hole {counter}: '))
    skor=int(input(f'Score on hole {counter}: '))
   
    if par>skor:
        if (par-skor)>3:
            print('invalid score')
        elif (par-skor)==3:
            print('albatross')
        elif (par-skor)==2:
            print('eagle')
        elif(par-skor==1):
            print('birdie')
    else:
        if(skor-par)==1:
            print('bogey')
        elif(skor-par)==2:
            print('double bogey')
        elif(skor-par)==3:
            print('triple bogey')
        elif (skor-par)>3:
            print('bad hole')
    if skor==par:
        print('par')
        
    counter+=1