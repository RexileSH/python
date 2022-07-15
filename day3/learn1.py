print("Welcome to the rollercoaster!")
height= float(input("What is your height in cm?"))
age=int(input("enter your age"))
if height>120:
    print("you can ride the rollercoaster!")
    if age <12:
     print ("your tecket price will be 5$")
    elif age <= 18:
        print("your tecket price will be 7$")
    else :
     print("your tecket price will be 12$")
else:
    print("sorry")