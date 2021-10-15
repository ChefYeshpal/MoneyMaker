# Sunil Money Maker Version 0.3
# First creation date : 3 feb 2021 
# Last updted date : 15 oct 2021
# Remarks 
# Using functions 

# Done
#  6 Use of Constants 

# Still need to do 
#  2 give profit % 
#  4 add transportation cost to give profit 
#  5 Keep last saved amount and add it to today money 

# StoryLine 
# You are a very poor person, and you some how managed to get hold of some money(legally) and you want to make more money, so you decide that you will sell waterbottles, when you check the price of one empty water bottle you get to know that it is of 1$''' ( AC - Actual cost)

# Purpose
# Make a program to sell water bottles 
#(bug)
# Ask 4 bottle sold twice
# Ask actual price of bottle only once

#################################################################################################################


# You have  x amount of money  
# This gets reset every time 
import random   
moneyToday = (random.randint(3,50))  # x 

def getMoney():
      print ("you have " + str(int(moneyToday)) + " INR today")    


## Costs associated ( Sample case)
# Bottle cost 2 INR 
# Filtering cost 8 paisa per bottle 
# Transportaion to Railway station : 40 Rs per day 
# Cost per ready to sell bottle = 2+0.08=2.08 Paisa
# Ask how much you will sell bottle for = 10 Rs per bottle
 
# Ask How many bottles you want to make today 
# def ride_bicycle():
#     print("\nHere's a bicycle. Have fun!\n")
bottMade = float(input("How many bottles you want to make today out of " + str(int(moneyToday/2.08)) + ": "))   # y 
def makeBottle():
     # Give error if exceeds possible number y which is x/2.08
     # later mater 
     # Loop it later 
     print("Processsing ... ")
     # wait for 3 seconds  -- later 
     import time
     time.sleep(3)
     # Made y number of bottles 
     print("Made " + str(int(bottMade)) + " bottles")
     # Bottles are ready to sell .. Happy selling. 
     print("Ready to sell bottles ---->>>>selling time >>>  " + str(int(bottMade)) + "")
     return bottMade
sellPrice = float(input("For how much > 2.08 do you want to sell your bottles for?: "))  # z 
bottSold = float(input("How many bottles you sold : "))  # n  ( make random)

def sellBottle():
     print("Processing ... ") 
     import time 
     time.sleep(3)
#work on this
# Check inventory should be y-n 
print ("Inventory should be " + str(int(bottMade - bottSold)) + ", is it ok ? ")
 # Check money box should be  n*10 
print ("Money box  should have " + str(int(bottSold*sellPrice)) + " INR, is it ok ? ")
  

def calcPL():
     if(2.8 > sellPrice):
      amount = 2.8 - sellPrice
      print(" You have a loss of {0} INR ".format(amount*bottSold))
     elif (sellPrice > 2.8):
      amount = sellPrice - 2.8
      print(" you have a profit of {0} INR ".format(amount*bottSold))
     else:
      print(" You have no profit nor loss")

getMoney()
makeBottle()
sellBottle()
calcPL()
