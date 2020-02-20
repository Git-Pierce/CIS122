def compute_square(num_to_square):
    return num_to_square * num_to_square


num = int(input("Enter a number to square: "))
num_squared = compute_square(num)
print("Num to square: ", num, ", squared is:", num_squared)