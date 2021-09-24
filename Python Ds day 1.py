# Program to find simple interest for given principal amount, time and rate of interest.

P = float(input("Enter the principal amount : "))
T = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
SI=(P * T * R)/100
print("Simple interest : {}".format(SI))