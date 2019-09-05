d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if d1>=1 and d1<=6 and d2>=1 and d2<=6:
    if d1+d2==7 or d1+d2==11:
        print('Winner')
    elif d1+d2==1 or d1+d2==3 or d1+d2==12:
        print('Loser')
    else:
        print(d1+d2)
else:
    print('Invalid input')


# Fill in the missing code below

#Accept d1 and d2, the number on two dices as input.
#First, check to see that they are in the proper range for dice (1-6).
#If not, print the message "Invalid input". Otherwise, determine the sum.
#If the sum is 7 or 11, print "Winner".
#If the sum is 2, 3 or 12, print "Loser". Otherwise print the sum.
