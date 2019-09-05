top_num = int(input("Upper number for the range: ")) # Do not change this line


for b in range(1, top_num):
    a=[]
    for i in range(1, b):
        if b%i==0:
            a.append(i)
    if sum(a)==b:
        print(b)
        
