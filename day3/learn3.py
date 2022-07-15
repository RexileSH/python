height = float(input("enter your height in m: "))
weight = float(input("enter your weight kg: "))

BMIf =int(weight)/float(height**2)
BMI=int(BMIf)
print(f"your bmi is {BMI}")

if BMI <18.5:
    print("underweight")
elif BMI <25 and BMI>18.5:
    print("normal weight")
elif BMI> 20 and BMI<30:
    print("obse")
elif BMI> 35:
    print("clinically obese")
else:
    print("wrong input")