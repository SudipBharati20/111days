# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number. 
# # Hint: Use the random module.
import random
class GuessingGame:
    def __init__(self, lower_bound=1, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.number_to_guess = random.randint(lower_bound, upper_bound)
        self.guess_count = 0

    def make_guess(self, guess):
        self.guess_count += 1
        if guess < self.number_to_guess:
            return "Higher number please"
        elif guess > self.number_to_guess:
            return "Lower number please"
        else:
            return f"Congratulations! You've guessed the number in {self.guess_count} guesses."