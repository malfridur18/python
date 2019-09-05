age = int(input("Input age: ")) # Do not change this line

if age>=65:
    print('The price is ', float(30*0.5))
elif age<=5:
    print('The price is ',float('0'))
else:
    print('The price is', float('30'))

# Fill in the missing code below

#Each ticket cost $30.
#Senior citizens (age >= 65) are given a 50% discount.
#Children under (or equal to) the age of 5 get a free admission.
#Write a program that prompts
#for the visitor's age and computes
#and prints the ticket price (which should be a float).
