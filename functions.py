Choosen = ["PIERRE", "FEUILLE", "CISEAUX"]

def UserName():
    """functions ask UserName"""
    user = input("quel est ton nom ? ")
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


