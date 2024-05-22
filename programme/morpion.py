#jeu du morpion
def jeu_du_morpion(pJoueur1 : str , pJoueur2 : str) -> list[str] :
    rslt : list[str]
    rslt =[]
    #regles
    print("Règles du jeu:\nPour jouer une partie de Morpion, chaque joueur à tour de rôle,\nplace un rond ou une croix dans une des cases de la grille.\n\nLe but du jeu est d'aligner trois croix ou ronds sur une même ligne.\n")

    joueur=1
    print("Le joueur 1 joue les X.Le joueur 2 joue les O")
    grille=[" "," "," "," "," "," "," "," "," "]
    afficher_la_grille(grille)

    #definition du statut de la partie:
    gagne=0
    while gagne==0:
        tour(grille,joueur)
        if gagnant(grille): #si la partie est remportée faire
            print("Le joueur "+str(joueur)+" remporte la partie")
            gagne=1

            if joueur == 1:
                rslt.append(pJoueur1)
                rslt.append(str(1))
            else :
                if joueur == 2:
                    rslt.append(pJoueur2)
                    rslt.append(str(1))
                    
            return rslt
        else:
            if match_nul(grille): #si il y a match nul
                print("Plus de place ! Match nul !")
                gagne=1
        if joueur==1:
            joueur=2
        else:
            joueur=1

def afficher_la_grille(grille):
    """ affichage de la grille de jeu séparée avec ses hauteurs
    """
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")
    print("   -------------")


def tour(grille, joueur):
    print("C'est le tour du joueur "+str(joueur))
    colonne=int(input("Entrez le numero de la colonne : "))
    while (colonne<0 or colonne>2):
        colonne=int(input("Entrez le numero de la colonne : "))
    ligne=int(input("Entrez le numero de la ligne : "))
    while (ligne<0 or ligne>2):
        ligne=int(input("Entrez le numero de la ligne : "))
    print("Vous avez joué la case",colonne,ligne)
    while grille[int(colonne)+int(ligne)*3]!=" ":
        afficher_la_grille(grille)
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=int(input("Entrez le numero de la colonne : "))
        if (colonne<0 or colonne>2):
            colonne=int(input("Entrez le numero de la colonne : "))
        ligne=int(input("Entrez le numero de la ligne : "))
        if (ligne<0 or ligne>2):
            ligne=int(input("Entrez le numero de la ligne : "))
        print("Vous avez joué la case","+",colonne,"+","+",ligne,"+")

    if joueur==1 :
        grille[int(colonne)+int(ligne)*3]="X"
    if joueur==2 :
        grille[int(colonne)+int(ligne)*3]="O"
    afficher_la_grille(grille)

def gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return 1

def match_nul(grille):
    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1