from decimal import FloatOperation

height= input("enter your height in m: ")
weight= input("enter your weight in KG: ")

BMIf =int(weight)/float(height)**2
BMI=int(BMIf)
print(BMI)