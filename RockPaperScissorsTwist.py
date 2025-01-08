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

##### inputs

#player decision
player_move = int(input("What do you chose?\nType '0' for Rock\nType '1' for Paper\nType '2' for Scissors\n"))
if player_move == 0:
    print(f"You threw rock.{rock}")
elif player_move == 1:
    print(f"You threw paper.{paper}")
elif player_move == 2:
    print(f"You threw scissors.{scissors}")
else:
    print("Please try again.")
    exit()


# rigged
if player_move == 2:
    computer_move = 0
else:
    computer_move = (player_move + 1)

#computer text
if computer_move == 0:
    print(f"Your opponent threw rock.{rock}")
elif computer_move == 1:
    print(f"Your opponent threw paper.{paper}")
elif computer_move == 2:
    print(f"Your opponent threw scissors.{scissors}")


##### Game outcome logic

# Tie Condition
if player_move == computer_move:
    print("Draw.")

# Player Win
elif (player_move == (computer_move + 1)) or (player_move == (computer_move - 2)):
    print("You win.")

# Computer Win
elif (player_move == (computer_move - 1)) or (player_move == (computer_move + 2)):
    print("You lose.")
