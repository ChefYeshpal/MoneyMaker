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

if y > x:
    print("this number is greater than " + str(int(x) + ""))
for x in x:
    if y < x:
        break
    print (y)
