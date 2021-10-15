number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value     : "))
power = 1

for i in range(1, exponent + 1):
    power = power * number
    
print("The number {0} with the power {1} is: {2}".format(number, exponent, power))