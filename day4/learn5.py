import random
rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_image=[rock,paper,scissors]

y=int(input("what do you choose? type 0 for rock , 1 for paper or 2 fo scissors "))
x=random.randint(0,2)
print("computer chose")
print(game_image[x])

if y==0 and x==2:
    print("you win")
elif y==0 and x==1:
    print ("lose")
elif y==1 and x==2:
    print("you lose")
elif y==1 and x==0:
    print("you win")
elif y==2 and x==0:
    print("you lose")
elif y==2 and x==1:
    print("ypu win")
else:
    print("same things")
