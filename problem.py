#We all have played snake, water gun game in our childhood. If you haven’t, google the 
#rules of this game and write a python program capable of playing this game with the 
#user.
import random
def snake_water_gun():
    options = ['snake', 'water', 'gun']
    computer_choice = random.choice(options)
    user_choice = input("Enter your choice (snake, water, gun): ").lower()

    if user_choice not in options:
        print("Invalid choice! Please choose snake, water, or gun.")
        return

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'snake' and computer_choice == 'water') or \
        (user_choice == 'water' and computer_choice == 'gun') or \
        (user_choice == 'gun' and computer_choice == 'snake'):
        print("You win!")
    else:
        print("Computer wins!")
snake_water_gun()
