#RPS GAME
import random
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      '1. Rock vs Paper -> Paper wins \n' 
      '2. Rock vs Scissors -> Rock wins \n'
      '3. Paper vs Scissors -> Scissors wins \n')
while True :
  print("Enter your choice \n 1-Rock \n 2-Paper \n 3-Scissors\n")

choice = int(input("Enter your choice: "))
while choice >3 or choice <1:
  chioce = int(input('Enter a calid choice please'))
  if choice == 1:
    choice_name ='Rock'
  elif choice == 2:
    choice_name = 'Paper'
  else:
    choice_name ='Scissors'