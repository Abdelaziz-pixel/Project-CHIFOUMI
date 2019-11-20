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
