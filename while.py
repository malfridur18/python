tala=input('input a number:')
itala=int(tala)
counter=0
while counter<itala:
    print(counter, end=' ') #madur getur radid hvad kemur a milli
    counter+=1
    if counter==5:
        break #nota break sparlega
else:
    print('Done')
