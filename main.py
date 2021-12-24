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
varibles = [rock, paper, scissors]

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if player_choose >= 3 or player_choose < 0:
    print("You typed an invaild number")
else:
    print(varibles[player_choose])

    computer_choose = random.randint(0,2)
    print("Computer chose:")
    print(varibles[computer_choose])

    if player_choose == 0 and computer_choose == 2:
        print("You win!")
    elif computer_choose == 0 and player_choose == 2:
        print("You win!")
    elif computer_choose > player_choose:
        print("You lose!")
    elif player_choose > computer_choose:
        print("You win!")
    elif computer_choose == player_choose:
        print("It's a draw!")
