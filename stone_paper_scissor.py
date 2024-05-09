answer = input(" Enter the value in capital Latters Rock Paper or scissor?:")
items = ["Paper", "Scissor", "Rock"]
item = ["Rock", "Paper", "Scissor"]

if answer == item[0]:
    print(items[0])
    print("You have lost this stage")

elif answer == item[1]:
    print(items[1])
    print("You have won")

elif answer == item[2]:
    print(items[2])
    print("You have lost again")

else:
    print("Enter the value according to the following!")
