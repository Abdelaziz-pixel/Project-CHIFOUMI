from random import randint
  
player = input('pierre (p), feuille (f) ou ciseaux (c)?')

if player == 'p':
  print('pierre', end=' ')
  
elif player == 'f':
  print('feuille', end=' ')
  
elif player == 'c':
  print('ciseaux', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if chosen == 1 :
  computer = 'p'
  print('pierre')
  
elif chosen == 2 :
  computer = 'f'
  print('feuille')
  
else:
  computer = 'c'
  print('ciseaux')

if player == computer:
  print('Égalité recommence!')
  
elif player == 'p' and computer == 'c':
  print('tu as gagné!')
  
elif player == 'p' and computer == 'f':
  print("l'ordinateur a gagné!")
  
elif player == 'f' and computer == 'p':
  print('tu as gagné!')
  
elif player == 'f' and computer == 'c':
  print("l'ordinateur a gagné!")

elif player == 'c' and computer == 'f':
  print('tu as gagné!')
  
elif player == "c" and computer == 'p':
  print("l'ordinateur a gagné!")

else:
  print('Choisit entre p, f, c et en minuscule')
  












