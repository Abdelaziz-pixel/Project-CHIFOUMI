from functions import *

Scores = {
  "User1": 0,
  "Computer1": 0
}

PlayerName = UserName()
while Scores["User1"] != 3 and Scores["Computer1"] != 3:

  User1 = Userchoice()

  Computer1 = ComputerChoice()

  TotalScores = Compare(User1, Computer1, Scores)

  print("Vous avez choisi {} ".format(User1))
  print("L'ordinateur a choisi {} ".format(Computer1))
  print("Vous avez:{} points | L'ordi à:{} points".format(Scores["User1"], Scores["Computer1"]))
