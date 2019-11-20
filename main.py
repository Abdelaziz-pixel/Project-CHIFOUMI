from functions import * """import functions of """

import os
import sys 
"""dictionnary who save scores of User1 and Computer1"""
Scores = {
  "User1": 0,
  "Computer1": 0
}

PlayerName = UserName() """call functions"""
while Scores["User1"] != 3 and Scores["Computer1"] != 3: """loop who compare scores User1 and Computer1"""

  User1 = Userchoice()

  Computer1 = ComputerChoice()

  TotalScores = Compare(User1, Computer1, Scores)

  print("Vous avez choisi {} ".format(User1)) """choice User1"""
  print("L'ordinateur a choisi {} ".format(Computer1)) """choice Computer1"""
  print("Vous avez: {} points | L'ordi à: {} points".format(Scores["User1"], Scores["Computer1"])) """compare choice """

  while Scores["User1"] == 3 or Scores["Computer1"] == 3: """loop for replay game"""
        rejouer = input("Voulez-vous rejouer ? oui/non").lower()
        if rejouer == "oui":
          """restart score at 0"""
            Scores["User1"] = 0 
            Scores["Computer1"] = 0 
        elif rejouer == "non":
            sys.exit()
        else:
          print("Veuillez choisir entre oui et non!")