print("welcome to treasure island your mission is to find the trasure")
way=input("right or left ?: ")
if way =="right":
    print("game over")
elif way=="left":
    way2=input("swim or wait? ")
    if way2 =="swim":
        print("game over")
    elif way2=="wait":
        way3=input("which door do you want red, blue, yallow? ")
        if way3=="blue":
            print("game over")
        elif way3=="red":
            print("game over")
        elif way3=="yallow":
            print("you win")

        else:
            print("wrong input")
    else:
        print("wrong input")    
else:
    print("wrong input")