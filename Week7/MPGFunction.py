def calculate_miles_per_gallon(miles_driven, gallons):
    mpg = miles_driven / gallons
    mpg = round(mpg, 1)
    return mpg

print("MPG: ", calculate_miles_per_gallon(100, 10))