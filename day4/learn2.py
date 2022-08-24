import random
from unicodedata import name
names_string = input("Give me everybody names, seprated by a comma. ")
names = names_string.split(",")
num_items = len(names)
random_choice = random.randint(0, num_items -1) 
print(random_choice)
person=names[random_choice]
print(person)
#بطريقة اخرى ل اختيار عشوائي
#person2=random.choice(names)
#yasprint(person2)

