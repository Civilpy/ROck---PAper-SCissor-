import random

print("rock ..." .lower())
print("paper ..." .lower())
print("scissors ..." .lower())
print("~~~~~~~~~~~~~~~~")

randomNumber = (random.randint(0,2))
computerMove = ''

if randomNumber == 0 :
    computerMove = "rock"
elif randomNumber == 1 :
    computerMove = 'paper'
elif randomNumber == 2:
    computerMove = "scissors"

# print(computerMove)
player_1_Wins= 0
player_2_Wins= 0
while player_1_Wins < 2 and player_2_Wins < 2 :
    print(f"player_1 wins : {player_1_Wins} and player_2 wins : {player_2_Wins}")

    player_1 = input('player_1 , make ur move :')
    print(f'player_2 , make ur move :  {computerMove}')
    player_2 = computerMove
    if player_1 == "End":
        break

    if player_1 == player_2:
        print("that\'s a tie")

    elif player_1 == "rock":
        if player_2 == 'scissors':
            print("player_1 wins !...")
            player_1_Wins += 1
        elif player_2 == 'paper':
            print('player_2 wins .......')
            player_2_Wins += 1 


    elif player_1 == "paper":
        if player_2 == 'scissors':
            print("player_2 wins !...")
            player_2_Wins += 1 
        elif player_2 == 'rock':
            print('player_1 wins .......')
            player_1_Wins += 1




    elif player_1 == "scissors":
        if player_2 == 'rock':
            print("player_2 wins !...")
            player_2_Wins += 1 
        elif player_2 == 'paper':
            print('player_1 wins .......')
            player_1_Wins += 1


    elif player_1 == player_2:
        print("that\'s a tie")
    else:
        print("something went wrong ....")

print(f"final scores : player_1 : {player_1_Wins} and player_2 : {player_2_Wins}")