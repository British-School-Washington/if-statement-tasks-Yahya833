# Set a secret number (you can change this value to anything)
secret_number = 7

# Ask the user to guess the secret number
guess = int(input("Guess the secret number: "))

while guess != secret_number:
    #if the guess is too high
    if guess > secret_number:
        print("too hig")
        guess = int(input("Try again: "))

    # if the guess is too low
    else:
        print("too low")
        guess = int(input("Try agian: "))




 # if the guess is correct
print("good job")
