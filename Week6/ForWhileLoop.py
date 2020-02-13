# Example of a For vs While loop
# investment growing at 5% each year
investment = int(input("Enter an amount you want to invest: "))
for i in range(5): # means 0 to 4
    interest = investment * .05
    investment += interest

print("Ending investment: ${}".format(round(investment, 2)))

numYears = 0
investment = int(input("Enter an amount you want to invest: "))
while numYears < 5:
    interest = investment * .05
    investment += interest
    numYears += 1
print("Ending investment: ", round(investment,2))

# Keep looping with investment and number of years
investment = int(input("Enter an amount you want to invest: "))
years = int(input("Enter the years you want to invest: "))
intRate = int(input("Enter your interest rate in whole numbers: "))
for i in range(years): # means 0 to 4
    interest = investment * intRate/100
    investment += interest
print("Ending investment: ${}".format(round(investment, 2)))