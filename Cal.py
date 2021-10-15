# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.SquareRt")
print("6.CubeRt")
print("-------------")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Calculating....")
        import time
        time.sleep(2)

        if choice == '1':
            print(num1, " added by ", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, " subtracted by ", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, " multiplied by ", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, " divided by ", num2, "=", divide(num1, num2))
        #work on this part
        elif choice == '5':
            import math
            number = (num1)
            number2 = (num2)
            sqrt = math.sqrt(number)
            sqrt = math.sqrt(number2)
            print("Square root of " + num1 + " is = " + number)
            print("Square root of " + num2 + " is = " + number2)
        break
    else:
        print("Invalid Input")
