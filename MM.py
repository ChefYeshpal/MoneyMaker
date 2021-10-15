# Sunil Money Maker Version 0.1 
# First creation date : 3 feb 2021 
# Last updted date : 3 fb 2021 
# Remarks 
# Still need to do 
#  1 Add dely in procesing 
#  2 give profit % 
#  3 Keep it in loop if user gives more number of bottls thn possible 
#  4 add transportation cost to give profit 
#  5 Keep last saved amount and add it to today money 
#  6 Use of Constants 

# StoryLine 
# You are a very poor person, and you some how managed to get hold of some money(legally) and you want to make more money, so you decide that you will sell waterbottles, when you check the price of one empty water bottle you get to know that it is of 1$'''

# Purpose
# Make a program to sell water bottles 
#################################################################################################################


# You have  x amount of money 
import random    
x = (random.randint(30,100))
print ("you have " + str(int(x)) + " INR today")
## Costs associated 
# Bottle cost 2 INR 
# Filtering cost 8 paisa per bottle 
# Transportaion to Railway station : 40 Rs per day 
# Cost per ready to sell bottle = 2+0.08=2.08 Paisa
# Ask how much you will sell bottle for = 10 Rs per bottle 

# Ask How many bottles you want to make today 
y = float(input("How many bottles you want to make today out of " + str(int(x/2.08)) + ": "))
# Give error if exceeds possible number y which is x/2.08
# later mater 
# Loop it later 

# GIve message for .. Processing. 
print("Processsing ... ")

# wait for 3 seconds  -- later 
# Made y number of bottles 
print("Made " + str(y) + " bottles")

# Bottles are ready to sell .. Happy selling. 
print("Ready to sell bottles  " + str(int(y)) + "")
# EoD proces 
# Are you closing today 
# ASK - How many bottle you sold - n 
n = float(input("How many bottles you sold : "))
if n > y :
    print("enter a number below " + str(int(y)) + "")  
    
    
# Check inventory should be y-n 
print ("Inventory should be " + str(int(y - n)) + " Is it ok ? ")
# Chck money box should be  n*10 
print ("Money box  should have " + str(int(n*10)) + " Is it ok ? ")
 
# PRofit margin is ???? \




