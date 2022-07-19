# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
pick = len(names)
name_picked = random.randint(0,pick-1)
print(names[name_picked] +" is going to buy the meal today!")



