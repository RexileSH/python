print("welcome to the rollercoaster")
height=int(input("what is your height "))
age=int(input("enter your age "))
bill=0
if height>120:
    print("you can ride the rollercoaster!")
    if age <12:
        bill=5
        print ("your tecket price will be 5$")
    elif age <= 18:
        bill = 7
        print("your tecket price will be 7$")
    elif age > 18 and age <45:
        bill = 12
        print("your tecket price will be 12$")
    elif age>= 45 and age <=55:
        print("your tecket will 0")
        bill=0
      
    wants_photo=input("do wany a photo taken ? Y or N. ")
    if wants_photo== "Y":
     bill+=3
     print(f"your final bill is {bill}")
    else:
        print(f"the total bill will be{bill} ")    
else:
    print("sorry")
    