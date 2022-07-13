from imghdr import what
print("welcome to the tip calculator")
x=float(input("what was the total bill? $"))
y=int(input("what percentage tip would you like to give? 10, 12, 15?"))
number_peoble=int(input("number of pepole"))
z=(x*(y/100))+x
pay=z/number_peoble
pay2=round(pay,3)
print(f"each person should pa :{pay2}")