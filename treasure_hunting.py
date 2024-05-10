# Print the welcome message
print("Welcome to the treasure island")

# Ask the user for their first choice
choice1 = input("Where do you want to go: left or right? ").lower()

# Check the first choice
if choice1 == 'right':
    # If the user chose right, ask for the second choice
    choice2 = input("Where do you want to go: swim or wait? ").lower()

    # Check the second choice
    if choice2 == 'wait':
        # If the user chose to wait, ask for the third choice
        choice3 = input("Which door do you want to go through: blue, yellow, or red? ").lower()

        # Check the third choice
        if choice3 == 'yellow':
            # If the user chose the yellow door, they win
            print("Congratulations! You have found the treasure and won!")
        else:
            # If the user chose a door other than yellow, they lose
            print("Sorry, you have chosen the wrong door. Game Over!")
    else:
        # If the user chose to swim, they lose
        print("Sorry, you chose to swim and got attacked by sea monsters. Game Over!")
else:
    # If the user chose left, they lose
    print("Sorry, you fell into a pit. Game Over!")
