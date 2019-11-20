import random

Choosen = ["PIERRE", "FEUILLE", "CISEAUX"] #"""choice list"""

def UserName():
    """functions ask UserName"""
    user = input("quel est ton nom ? ")
    print("Bienvenue ! Je te souhaite un bon courage {} ".format(user))
    while ControlName(user) is False:
        print("Votre nom doit contenir au moins 2 caractéres")
        user = input("Quel est ton nom ? ")
    return user 

def ControlName(user):
    """functions control name"""
    try:
        assert len(user) > 2 
    except AssertionError as a:
        return False

def Userchoice():
    """user choice value"""
    print("Choisissez entre PIERRE, FEUILLE, CISEAUX")
    PlayerChoice = input("Votre choix est ").upper()
    while ControlChoice(PlayerChoice) is False:
        print("Choisissez entre PIERRE, FEUILLE, CISEAUX")
        PlayerChoice = input("Votre choix est ").upper()
    return PlayerChoice

def ControlChoice(PlayerChoice):
    """function for control choice"""
    try:
        assert PlayerChoice in Choosen
    except AssertionError as a:
        return False

def ComputerChoice():
    """functions choice computer"""
    return Choosen[random.randint(0, len(Choosen)-1)]

def Compare(User1, Computer1, Scores):
    """compare choice User1 and Computer1 and add Scores"""
    if User1 != Computer1:
        if User1 == "PIERRE" and Computer1 == "CISEAUX"\
        or User1 == "FEUILLE" and Computer1 == "PIERRE"\
        or User1 == "CISEAUX" and Computer1 == "FEUILLE":
            Scores["User1"] += 1
        else:
            Scores["Computer1"] += 1
    return Scores 
