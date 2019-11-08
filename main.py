from random import randint

UserChoice = input("what you name ?") #we ask for the first name of the user
print("hey, {}, we do a part ?".format(UserChoice)) #welcome message with user's first name

score_file = open("scores.txt", "a+") #method to store the scores

UserChoice = input('stone (r), paper (p) ou scissors (s)?') #the user is offered three choices represented by the keys of the keyboard

if UserChoice == 'r':
  print('stone', end=' ') #display of the user's choice
  
elif UserChoice == 'p':
  print('paper', end=' ')
  
elif UserChoice == 's':
  print('scissors', end=' ')
  
else: #error message
  print('??')
  
print('vs', end=' ')

ComputerChoice = randint(1,3)

#display of the choice of the computer
if ComputerChoice == 1 : 
  computer = 'r'
  print('stone')
  
elif ComputerChoice == 2 :
  computer = 'p'
  print('paper')
  
else:
  computer = 's'
  print('scissors')

#comparison of the choice of the user and the choice of the computer and recording of the score
if UserChoice == computer:
  print('Equality begins again!')
  print('Equality begins again!', file = score_file)
  
elif UserChoice == 'r' and computer == 's':
  print('you won!')
  print('you won!', file = score_file)
  
elif UserChoice == 'r' and computer == 'p':
  print("the computer won!")
  print("the computer won!", file = score_file)
  
elif UserChoice == 'p' and computer == 'r':
  print('you won!')
  print('you won!', file = score_file)
  
elif UserChoice == 'p' and computer == 's':
  print("the computer won!")
  print("the computer won!", file = score_file)

elif UserChoice == 's' and computer == 'p':
  print('you won!')
  print('you won!', file = score_file)
  
elif UserChoice == "s" and computer == 'r':
  print("the computer won!")
  print("the computer won!", file = score_file)

else:
  print('choose between r, p, s and lowercase')

score_file.close() #closing the score registration method
  












