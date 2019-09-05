import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

# convert strings to ints
x1_int=int(x1_str)
y1_int=int(y1_str)
x2_int=int(x2_str)
y2_int=int(y2_str)

#first=(y1_int-x1_int)**2
#second=(y2_int-x2_int)**2
#both=first+second
d=math.sqrt(((y1_int-x1_int)**2)+((y2_int-x2_int)**2))
#  d =
print("d =",d)  # do not change this line
