weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line
weight_int=int(weight_str)
height_int=int(height_str)/100
#height_meters=height_int/100
bmi=weight_int/(height_int**2)

print("BMI is: ", bmi) # do not change this line
