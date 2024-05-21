import random

def game():
    choices = ['stone', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (stone, paper, scissors): ")
    print("Computer chose: ", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'stone' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'stone'):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    while True:
        game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break