# Ask the user to enter their score (0-100)
score = int(input("Enter your score: "))

# if the score is 90 or above
if score >= 90:
    grade = "a"

# if the score is between 80 and 89
elif score >= 80:
    grade = "b"

# if the score is between 70 and 79
elif score >= 70:
    grade = "c"

# if the score is below 70
else:
    grade = "fail!!!!!"

print(f"You got a ",grade)