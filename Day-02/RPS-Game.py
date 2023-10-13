import random
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      '1. Rock vs Paper -> Paper wins \n' 
      '2. Rock vs Scissors -> Rock wins \n'
      '3. Paper vs Scissors -> Scissors wins \n')
while True :
  print("Enter your choice \n 1-Rock \n 2-Paper \n 3-Scissors")
  choice = int(input("Enter your choice: "))
  while choice >3 or choice <1:
    choice = int(input('Enter a valid choice please'))
  if choice == 1:
    choice_name ='Rock'
  elif choice == 2:
    choice_name = 'Paper'
  else:
    choice_name ='Scissors'
    comp_choice = random.randint(a:1, b:3)

  while comp_choice == choice:
    comp_choice = random.randint(a:1, b:3)
  if comp_choice == 1:
   comp_choice_name ='rock'
  elif comp_choice == 2:
   comp_choice_name ='paper'
  else:
   comp_choice_name = 'scissors'
  print("Computer choice is \n", comp_choice_name)
  print(choice_name, 'Vs', comp_choice_name)

  if choice == comp_choice:
   print("It's a draw", end ="")
   result = "DRAW"


if(choice ==1 and comp_choice == 2):
  print('paper wins =>',end ="")
  result = "papeR"
elif(choice ==2 and comp_choice == 1):
  print('rock wins =>',end ="")
  result = "PAPER"

if(choice==1 and comp_choice ==3):
  print('Rock wins =>\n', end ="")
  result = "Rock"
elif(choice==3 and comp_choice == 1):
  print('Rock wins =>\n', end ="")
  result ="rock"
  
if(choice==2 and comp_choice ==3):
  print('Scissors wins =>\n', end ="")
  result = "scissoR"
elif(choice == 3 and comp_choice==2):
  print('Scissors wins =>', end ="")
  result = 'scissor'

if result =='DRAW':
  print("<== It's a tie ==>")
if result == choice_name:
  print("<== User wins ==>")
else:
  print("<== Computer wins ==>")
  