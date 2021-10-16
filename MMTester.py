
'''import random   
moneyToday = (random.randint(3,50))  # x 

print ("you have " + str(int(moneyToday)) + " INR today")

 
# Ask How many bottles you want to make today 

bottMade = float(input("How many bottles you want to make today out of " + str(int(moneyToday/2.08)) + ": ")) '''  # y 
     # Give error if exceeds possible number y which is x/2.08
     # later mater 
     # Loop it later

#random amount of money between 3 to 50
import random   
moneyToday = (random.randint(3,50))  # x 

print ("you have " + str(int(moneyToday)) + " INR today")

#2.08 is cost of 1 shovel
BM1 = moneyToday/2.08

#how many shovels to make out of "moneyToday"?(user input)
shovMade = float(input("How many bottles you want to make today out of " + str(int(moneyToday/2.08)) + ": "))

#####this loop does not work (I need help in this)#####
if shovMade > BM1:
    input("Please put a number below " + str(int(moneyToday/2.08)) + ": ")

else:
    print("tadaa, it works!!!")

