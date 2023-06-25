height = input("Please enter your height in m: ")
weight = input("Please enter your weight in kg: ")

#convert to int
weight_as_int = int(weight)
#convert to float
height_as_float = float(height)

#using the exponent operator **
bmi = weight_as_int / height_as_float**2

bmi_as_int = int(bmi)

#convert to str for concatenate
print("Your BMI is : " + str(bmi_as_int))