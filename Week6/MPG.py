# Calculate MPG using a while loop
moreData = "y"
milesDriven = float(input("Enter miles driven: "))
gallonsUsed = float(input("Enter gallons used: "))

while moreData:

    if (milesDriven > 0 and  gallonsUsed > 0):

        mpgUsed = milesDriven / gallonsUsed
        print("Mpg is: ", round(mpgUsed, 2))
        moreData = input("Do you want to enter more MPG values?")
        if moreData.lower() == 'n':
            print("OK the program will now exit!")
            break;
        else:
            milesDriven = float(input("Enter miles driven: "))
            gallonsUsed = float(input("Enter gallons used: "))
    else: # both values are 0
        print("Miles entered and gallons used must be greater than 0")
        moreData = input("Do you want to enter more MPG values?")
        if moreData.lower() == "y":
            milesDriven = float(input("Enter miles driven: "))
            gallonsUsed = float(input("Enter gallons used: "))
        else:
            print("OK the program will now exit!")
            break;


