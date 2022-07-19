print("welcome to python pizza")
size = input("what size pizza do yo wnat S,M,L")
add_pepperoni= input("do you want pepperoni? Y,N")
extra_cheese= input("Do you want extra cheese Y or N")
bill=0
if size =="S":
    print("you price will be 15$")
    bill=15
    if add_pepperoni =="Y":
        print("add pepperoni +2$")
        bill=bill+2
elif size=="M":
    print("you price will be 20$")
    bill=20
elif size=="L":
    print("your price will be 25$")
    bill=25
    if add_pepperoni =="Y":
        print("add pepperoni +3$")
        bill=bill+3
    else:
        print("okay")
else:
    print("wrong input")
if extra_cheese =="Y":
    print("add chesse +1")
    bill=bill+1  
print(f"total price will be {bill}")
