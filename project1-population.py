ar=int(input('Years:'))
folk=307357870
if ar<0:
    print('Invalid input!')
else:
    folk2=folk+float(ar*4505142.857)-float(ar*2425846.154)+float(ar*901028.5714)
    print('New popoulation after ',ar,'years is ', int(folk2))
    
