import random
def main():
    print('Let\'s play Rock, Paper Scissors!')
    player_choice = input("Enter a choice: rock, paper, or scissors ").lower()
    while player_choice not in ['rock','paper','scissors']:
        print("Invalid choice, please ", end="")
        player_choice = input("enter a choice: rock, paper, or scissors ").lower()
    computer_choice = random.choice(['rock','paper','scissors']).lower()
    if player_choice == computer_choice:
        print("It is a tie!")
    elif(player_choice == 'rock' and computer_choice == 'paper') or \
        (player_choice == 'paper' and computer_choice == 'scissors') or \
        (player_choice == 'scissors' and computer_choice == 'rock'):
        print(f"Computer wins as {computer_choice} beats {player_choice}!")
    else:
        print(f'User wins as {player_choice} beats {computer_choice}!')
    if('y' == input("Would you like to play again? (y/n)")[0].lower()):
        main()
if __name__ == '__main__':
    main()