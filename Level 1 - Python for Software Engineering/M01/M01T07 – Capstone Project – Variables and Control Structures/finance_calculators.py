import math

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.\n")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").strip().lower()

if user_choice == "investment":
    principal = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage, e.g., 8): "))
    years = float(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter interest type ('simple' or 'compound'): ").strip().lower()

    r = interest_rate / 100

    if interest_type == "simple":
        total_amount = principal * (1 + r * years)
        print(f"\nTotal accumulated amount after {years:.0f} years: R{total_amount:.2f}")
    elif interest_type == "compound":
        total_amount = principal * math.pow((1 + r), years)
        print(f"\nTotal accumulated amount after {years:.0f} years: R{total_amount:.2f}")
    else:
        print("\nError: Invalid interest type entered. Please enter either 'simple' or 'compound'.")

elif user_choice == "bond":
    house_value = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage, e.g., 7): "))
    months = float(input("Enter the number of months to repay the bond: "))

    monthly_interest = (annual_rate / 100) / 12

    repayment = (monthly_interest * house_value) / (1 - math.pow((1 + monthly_interest), -months))

    print(f"\nMonthly bond repayment amount: R{repayment:.2f}")

else:
    print("\nError: Invalid selection! Please restart and enter either 'investment' or 'bond'.")