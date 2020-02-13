# The Test Scores program with loops

print("The Test Scores program")
print()
print("Enter 999 to end the program")
print("============================")

# init variables
count = 0
testScore = 0
totalScore = 0

testScore = int(input("Enter a valid test score: "));
while testScore < 999:

    # if testScore == 999:
    #     break;
    if (testScore >= 0 and testScore <= 100):
       totalScore += testScore
       count += 1
    else:
        print("Test score must be <= 100.  Pls try again!")
    testScore = int(input("Enter a valid test score: "))


# calculate average score
avgScore = totalScore/count

# print out the score
print("Average Score: ", avgScore,
      "Total Score: ", totalScore)
print()