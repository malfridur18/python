high_number=int(input('sladu inn tolu: '))
for i in range(1,high_number+1):
    if i%3==0:
        if i%5==0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i%5==0 and i%3!=0:
        print('Buzz')
    else:
        print(i)
    