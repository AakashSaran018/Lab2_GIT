import random


def main():
    print("Welcome to Rock Paper Scissors!")
    print()
    print("Rules:")
    print("Rock beats scissors.")
    print("Scissors beats paper.")
    print("Paper beats rock.")
    print("If both players choose the same option, it is a tie.")
    print()

    choices = ("rock", "paper", "scissors")

    player = input("Enter your choice (rock, paper, or scissors): ")

    while True:
        
        computer = random.choice(choices)

        print("Computer chose:", computer)

        if player == computer:
            print("It's a tie! The computer will choose again.")
            continue

        elif (player, computer) in (
            ("rock", "scissors"),
            ("paper", "rock"),
            ("scissors", "paper")
        ):
            print("You win!")

        else:
            print("Computer wins!")

        break


if __name__ == "__main__":
    main()