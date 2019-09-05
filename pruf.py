
for j in range(1,100):
    counter=0
    for k in range(1,100):
        if j%k==0:
            counter+=1
    if counter==10:
        print(j)

