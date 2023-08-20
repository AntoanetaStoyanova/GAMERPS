import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]  #list , collections of elements, here we have multiple strings store in this list
#access one of the elements of the list 
#options[0] # in this case it's rock

while True:
    user_input = input("Type Rock, Paper or Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:   #list
        continue 

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":  # the AND check if the condition on the left side and the condition on the right side are true/ if i use OR it will check if either the left or the right is true, or both of them are true  
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":  # the AND check if the condition on the left side and the condition on the right side are true/ if i use OR it will check if either the left or the right is true, or both of them are true  
        print("You won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":  # the AND check if the condition on the left side and the condition on the right side are true/ if i use OR it will check if either the left or the right is true, or both of them are true  
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")



