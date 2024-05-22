def addToScore(pseudo : str, score : str, liste : list[list[str]] ):
    """ ajoute un score qui est associé à un pseudo 
    """
    el : list[str]
    i : int 
    i = 0
    chgt : bool
    chgt = False
    while (not chgt and i < len(liste)) :
        el = liste[i]
        if el[0] == pseudo :
            el[1] = score
            print("le score du joueur ", pseudo, "a été changé. Le nouveau score est : ", score, " points.")
            chgt = True
        else:
            i += 1
    if not chgt :
        liste.append([pseudo, score])
        print("Une nouvelle entrée au nom de ", pseudo, " a été ajoutée")
        print("Meilleur score actuel : ", score, " points")

def affichescore(pseudo : str, liste : list[list[int]]):
    """
    procédure affichant le score d'un pseudo pour un jeu spécifique
    """
    chgt : bool
    i : int
    el : list[str]
    i = 0
    chgt = False
    while (not chgt and i < len(liste)):
        el = liste[i]
        if el[0] == pseudo :
            print ("le score de ", pseudo, " est de: ", el[1], " points")
            chgt = True
        else: 
            i += 1
    if (not chgt) : 
        print ("erreur, le pseudo ", pseudo, "n'a pas été trouvé")

def triescores(liste: list[list[str]]):
    temp : list[str]
    temp = []
    for i in range(len(liste) - 1):
        if (liste[i][1] > liste[i+1][1]):
            temp = liste[i]
            liste[i]
            liste[i+1] = temp
        print("scores triés")

def afficheTableauScores(liste : list[list[str]]):
    el : list[str]
    for el in liste : 
        print (r"""
 ____   __    ____  __    ____    __    __  __    ____  ____  ___    ___   ___  _____  ____  ____  ___   
(_  _) /__\  (  _ \(  )  ( ___)  /__\  (  )(  )  (  _ \( ___)/ __)  / __) / __)(  _  )(  _ \( ___)/ __)  
  )(  /(__)\  ) _ < )(__  )__)  /(__)\  )(__)(    )(_) ))__) \__ \  \__ \( (__  )(_)(  )   / )__) \__ \  
 (__)(__)(__)(____/(____)(____)(__)(__)(______)  (____/(____)(___/  (___/ \___)(_____)(_)\_)(____)(___/  
               """)
        print("joueur : ", el[0], " - score: ", el[1])
        print("______________________________________")