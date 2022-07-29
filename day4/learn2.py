import random
from unicodedata import name
names_string = input("Give me everybody names, seprated by a comma. ")
names = names_string.split(",")
num_items = len(names)
random_choice = random.randint(0, num_items -1) 
person=names[random_choice]
print(person)
print(num_items)
 #بطريقة اخرى ل اختيار عشوائي
person2=random.choice(names)
print(person2)

