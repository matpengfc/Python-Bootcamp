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
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if human_choice == 0:
#   print(rock)
# elif human_choice == 1:
#   print(paper)
# else:
#   print(scissors)

game_images = [rock, paper, scissors]  # 0,1,2 by order of the list (using list to replace if/else)
# O win to 2, 0 lose to 1, 1 lose to 2
# computer random choice
import random
computer_choice = random.randint(0,2)

# if computer_choice == 0:
#   print(rock)
# elif computer_choice == 1:
#   print(paper)
# else:
#   print(scissors)

if human_choice >= 3 or human_choice < 0:
  print("Invalid Human Choice")
else:
  print(game_images[human_choice])
  print(f"Computer choose: {game_images[computer_choice]}")
  if human_choice == computer_choice:
    print("Draw")
  elif human_choice - computer_choice == 1 or computer_choice - human_choice == 2:
    print("Human Win")
  else:
    print("Computer Win")