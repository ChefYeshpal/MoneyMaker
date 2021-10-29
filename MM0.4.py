# Sunil Money Maker Version 0.4
# First creation date : 3 feb 2021 
# Last updted date : 18 oct 2021
# Remarks 
# Using functions 
#loop is working

# Done
#  loop finally work!!!
# Ask 4 bottle sold twice
# Ask actual price of bottle only once 
# Selling amount of bottle is Randomly selected

# Still need to do 
#  2 give profit % 
#  4 add transportation cost to give profit 
#  5 Keep last saved amount and add it to today money 

# StoryLine 
# You are a very poor person, and you some how managed to get hold of some money(legally) and you want to make more money, so you decide that you will sell waterbottles, when you check the price of one empty water bottle you get to know that it is of 1$''' ( AC - Actual cost)

# Purpose
# Make a program to sell water bottles 

#(bugs)


#################################################################################################################


# You have  x amount of money  
# This gets reset every time 

while True:
     import random   
moneyToday = (random.randint(3,50))  # x 

print ("you have " + str(int(moneyToday)) + " INR today")


## Costs associated ( Sample case)

# Bottle cost 2 INR 
# Filtering cost 8 paisa per bottle 
# Transportaion to Railway station : 40 Rs per day 
# Cost per ready to sell bottle = 2+0.08=2.08 Paisa
# Ask how much you will sell bottle for = 10 Rs per bottle
 
# Ask How many bottles you want to make today 
maxBott = int(moneyToday/2)
bottMade = int(input("How many bottles you want to make today out of " + str(int(moneyToday/2.08)) + ": "))   # y 
     # Give error if exceeds possible number y which is x/2.08
     # later mater 
     # Loop it later 
while bottMade > maxBott : 
     bottMade = int(input("How many bottles you want to make today out of " + str(int(moneyToday/2.08)) + ": "))   # y
     if bottMade <= maxBott:
          break

print("Creating Bottles ... ")
     # wait for 3 seconds  -- later 
import time
time.sleep(3)


     # Made y number of bottles 
print("Made " + str(int(bottMade)) + " bottles")
     # Bottles are ready to sell .. Happy selling. 
print("Ready to sell bottles " + str(int(bottMade)) + "")
print("----Selling time----")
     #return bottMade
sellPrice = float(input("For how much >2 do you want to sell your bottles for?: "))  # z




print("Selling bottles ... ")
     # wait for 3 seconds  -- later 
import time
time.sleep(3)

#Bottle sold

import random   
bottSold = (random.randint(0,bottMade))  # x 

if bottSold > 1:
    print("you sold " + str(int(bottSold)) + " bottle's")

else :
    print("you sold " + str(int(bottSold)) + " bottle")


#EoD Process
#work on this
# Check inventory should be y-n 
print ("Inventory is " + str(int(bottMade - bottSold)) + ", is it ok ? ")
 # Check money box should be  n*10 
print ("Money box has " + str(int(bottSold*sellPrice)) + " INR, is it ok ? ")

print("Calculating profit or loss ...")

import time
time.sleep(3)
  

if(2.8 > sellPrice):
      amount = 2.8 - sellPrice
      print(" You have a loss of {0} INR ".format(amount*bottSold))
elif (sellPrice > 2.8):
      amount = sellPrice - 2.8
      print(" you have a profit of {0} INR ".format(amount*bottSold))
else:
      print(" You have no profit nor loss")

print("end of day one")

if check.upper() == "x":
     quit

print("Quitted")

#getMoney()
#makeBottle()
#sellBottle()
#calcPL()
