import ten_number

def guess_the_number():
    print("Guess my number between 1 and 1000 with the fewest guesses:")
    number_to_guess = random.randint(1, 1000)
    attempts = 0
    guess = 0

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print("Congratulations. You guessed the number!")
            print("It took you", attempts, "guess(es).")

play_again = "yes"
while play_again == "yes" or play_again == "y":
    guess_the_number()
    play_again = input("Would you like to play again? (yes/no): ").lower().strip()

print("Thanks for playing!")
