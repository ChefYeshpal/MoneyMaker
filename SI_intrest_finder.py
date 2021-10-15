princ_amount = float(input("Enter the principle amount  : "))
rate_of_int = float(input("Enter the rate of intrest    : "))
time_period = float(input("nter the time period(annually: )"))
SI = (princ_amount*rate_of_int*time_period)/100
print("sample intrest for principal amount: {1}".format(princ_amount, SI))