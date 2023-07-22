import math

print("This is a finance calculator to calculate the value of your investment or the value of your bond")
print("Please choose an option:")
print("1. Investment")
print("2. Bond")

option = input("Enter your choice (Investment/Bond): ")

if option.lower() == 'investment':
    print("You have selected the investment calculator.")
    #variables
    principal = float(input("Please enter the amount of money that you are investing: "))
    rate = float(input("Please enter the interest rate (as a percentage): "))
    duration = float(input("Please enter the number of years you plan to invest: "))
    interest_type = input("Do you want 'simple' or 'compound' interest? ")

    #convert the rate from a percentage to a decimal
    rate = rate / 100
#investment calculation
    if interest_type.lower() == 'simple':
        total = principal * (1 + rate * duration)
    elif interest_type.lower() == 'compound':
        total = principal * ((1 + rate) ** duration)

    print(f"Your investment will grow to: {total}")

elif option.lower() == 'bond':
    print("You have selected the bond repayment calculator.")
    principal = float(input("Please enter the present value or cost of the house: "))
    interest_rate = float(input("Please enter your annual interest rate (as a percentage): "))
    years = float(input("Please enter the number of years you plan to repay the bond: "))

    #convert the interest rate from percentage to a proportion and make it monthly
    monthly_interest_rate = (interest_rate / 100) / 12
    #convert years to months
    months = years * 12

    #calculate the bond repayment
    repayment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / ((1 + monthly_interest_rate) ** months - 1)

    print(f"Your bond repayment will be: {repayment} per month.")
else:
    print("Invalid option. Please choose either 'Investment' or 'Bond'.")