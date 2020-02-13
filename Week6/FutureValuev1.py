#simpler version of the future value calculation
# using fixed values

monthlyInvestment = 100
monthlyIntRate = .10/12
numMonths = 120
futureValue = 0

for month in range(numMonths):
    futureValue += monthlyInvestment
    monthlyIntAmount = futureValue * monthlyIntRate
    futureValue += monthlyIntAmount

print("Future Value: ${}".format(round(futureValue, 2)))

# rewrite this program using input for each of the variables