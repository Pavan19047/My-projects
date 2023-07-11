import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("What do you choose, Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

computer_choice = random.randint(0,2)


if user_choice == 0 and computer_choice == 1:
  print(f"You choose{user_choice}\n")
  print(f"{rock}\n")
  print(f"Computer chose {computer_choice}\n")
  print(f"{paper}\n")
  print("Computer wins")

elif user_choice == 0 and computer_choice == 2:
  print(f"You choose {user_choice}\n")
  print(f"{rock}\n")
  print(f"Computer chose {computer_choice}\n")
  print(f"{scissors}\n")
  print("You win")

elif user_choice == 1 and computer_choice == 0:
  print(f"You choose {user_choice}\n")
  print(f"{paper}\n")
  print(f"Computer chose {computer_choice}\n")
  print(f"{rock}\n")
  print("You win")

elif user_choice == 1 and computer_choice == 2:
  print(f"You choose {user_choice}\n")
  print(f"{paper}\n")
  print(f"Computer chose {computer_choice}\n")
  print(f"{scissors}\n")
  print("Computer wins")

elif user_choice == 2 and computer_choice == 0:
  print(f"You choose {user_choice}\n")
  print(f"{scissors}\n")
  print(f"Computer chose {computer_choice}\n")
  print(f"{rock}\n")
  print("Computer wins")

elif user_choice == 2 and computer_choice == 1:
  print(f"You choose {user_choice}\n")
  print(f"{scissors}\n")
  print(f"Computer chose {computer_choice}\n")
  print(f"{paper}\n")
  print("Computer wins")

elif user_choice == computer_choice:
  print("It's a Tie")
  
  #Solution
  
  
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")