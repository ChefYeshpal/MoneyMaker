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
x = (random.randint(40,100))
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

z = float(input("For how much do you want to sell your bottles for?: "))

# GIve message for .. Processing. 
print("Processsing ... ")

# wait for 3 seconds  -- later 
import time
time.sleep(3)
# Made y number of bottles 
print("Made " + str(int(y)) + " bottles")

# Bottles are ready to sell .. Happy selling. 
print("Ready to sell bottles  " + str(int(y)) + "")
# EoD proces 
# Are you closing today 
# ASK - How many bottle you sold - n 
#n = float(input("How many bottles you sold : "))

'''if n > y :
    float(input("enter a number below " + str(int(y)) + ": "))
while True :
    try :
        n = float(input("enter a number below " + str(int(y)) + ": "))
    except ValueError :
        float(input("enter a number below " + str(int(y)) + ": "))
    else :
        break'''
'''elif y > n :
    print("processing...")
    import time
    time.sleep(2)'''
#looped
while True :
    try :
        n = int(input("How many bottles you sold: "))
    except ValueError :
        int(input("Enter a number below " + str(int(y)) + ": "))
        continue
    if n > y :
        int(input("Enter a number below " + str(int(y)) + ": "))
        continue
    else :
        break
    
# Check inventory should be y-n 
print ("Inventory should be " + str(int(y - n)) + ", is it ok ? ")
# Check money box should be  n*10 
print ("Money box  should have " + str(int(n*z)) + " INR, is it ok ? ")
 
# PRofit margin is ???? \
#AC = int(2.8)
AC = float(input("what do you think was the actual price of the bottles?: "))
SA = float(input("for how much did you sell your bottles for?: "))

if(2.8 > z):
    amount = AC - SA
    print("your loss amount is {0}".format(amount))
elif (SA > AC):
    amount = SA - AC
    print("your profit amount is {0}".format(amount))
else:
    print("you have no loss no profit!!!")

