# Programme : Puissance 4
# - demande aux joueurs à tour de role dans quelle colonne il veulent jouer
# - détecte une colonne pleine
# - détecte la grille pleine
# - détecte 4 pions alignés verticalement
# - détecte 4 pions (ou plus) alignés horizontalement
# - détecte 4 pions (ou plus) alignés en diagonale croissante
# - détecte 4 pions (ou plus) alignés en diagonale décroissante
# - filtre la saisie de l'utilisateur et envoie un message sur la sortie standard si la saisie est erronée


# Structure de donnée mémorisant la grille : une liste à 2 dimensions (6 lignes et 7 colonnes) contenant :
# - un 0 si la case est vide
# - un 1 si un pion ROUGE est dans la case
# - un 2 si un pion BLEU est dans la case

grille=[7*[0], 7*[0], 7*[0], 7*[0], 7*[0], 7*[0]]

""" Repérage des éléments dans la grille :

élément grille[0][0] (coin supérieur gauche) :
[[X, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]

élément grille[0][6] (coin supérieur droit) :
[[0, 0, 0, 0, 0, 0, X],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]

élément grille[5][0] (coin inférieur gauche) :
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [X, 0, 0, 0, 0, 0, 0]]

élément grille[5][6] (coin inférieur droit):
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, X]]

 """

# tab_colonne mémorise le nombre de pions dans chacune des colonnes
tab_colonne=7*[0]
# joueur_courant indique le prochain joueur qui doit jouer : 1 pour ROUGE et 2 pour BLEU
joueur_courant=1

# La fonction afficher_grille() affiche la grille sur la sortie standard
def afficher_grille():
    for i in range(6):
        print(grille[i])

    # affiche le repère des colonnes sous la grille :
    print('\n 0  1  2  3  4  5  6')

# La fonction grille_pleine() teste si la grille est pleine (aucun 0 dans la liste grille)
def grille_pleine():
    b_plein=True
    for i in range(6):
        for j in range(7):
            if grille[i][j]==0:
                b_plein=False
    return b_plein

# La fonction pions_alignes() teste si 4 pions de même couleur sont alignés dans la grille
def pions_alignes():
    trouve=0
    # teste 4 pions alignés horizontalement en alanysant chacune des 6 lignes :
    for i in range(6):
        rouge=0
        bleu=0
        for j in range(7):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    return trouve
            else:
                rouge=0
                bleu=0
    # teste 4 pions alignés verticalement en alanysant chacune des 7 colonnes :
    for j in range(7):
        rouge=0
        bleu=0
        for i in range(6):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    return trouve
            else:
                rouge=0
                bleu=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste les 6 diagonales croissantes :
    """
    [0, 0, 0, X, X, X, X]
    [0, 0, X, X, X, X, X]
    [0, X, X, X, X, X, X]
    [X, X, X, X, X, X, 0]
    [X, X, X, X, X, 0, 0]
    [X, X, X, X, 0, 0, 0]

    On part d'une case de départ (D ci-dessous) puis on incrémente les indices en diagonale jusqu'à atteindre l'indice maximal de la grille :

    grille[i][j] (i=n° de la ligne de 0 à 5 et j=n° de la colonne de 0 à 6)

j :  0  1  2  3  4  5  6
    [0, 0, 0, X, X, X, X] 0
    [0, 0, X, X, X, X, X] 1
    [0, X, X, X, X, X, X] 2
    [D, X, X, X, X, X, 0] 3
    [D, X, X, X, X, 0, 0] 4
    [D, D, D, D, 0, 0, 0] 5
                          i

    Analyse du problème :
    Il y a :
        2 diagonales à 4 cases (ij) : 30 21 12 03 et 53 44 35 26
        2 diagonales à 5 cases (ij) : 40 31 22 13 04 et 52 43 34 25 16
        2 diagonales à 6 cases (ij) : 50 41 32 23 14 05 et 51 42 33 24 15 06

    Dans les 6 cas j est croissant (analyse des diagonales de gauche à droite) et i est une fonction de j :

    diagonale à 4 cases (ij) 30 21 12 03 : j de 0 à 3 et i=3-j
    diagonale à 4 cases (ij) 53 44 35 26 : j de 3 à 6 et i=8-j

    diagonale à 5 cases (ij) 40 31 22 13 04 : j de 0 à 4 et i=4-j
    diagonale à 5 cases (ij) 52 43 34 25 16 : j de 2 à 6 et i=7-j

    diagonale à 6 cases (ij) 50 41 32 23 14 05 : j de 0 à 5 et i=5-j
    diagonale à 6 cases (ij) 51 42 33 24 15 06 : j de 1 à 6 et i=6-j

    Optimisons : le compteur de base est j, les 3 autres sont fonction de j :

    diagonale à 4 cases (ij) 30 21 12 03 : j de 0 à 3 et i=3-j
    diagonale à 4 cases (kl) 53 44 35 26 : k=i+2 et l=j+3

    diagonale à 5 cases (ij) 40 31 22 13 04 : j de 0 à 4 et i=4-j
    diagonale à 5 cases (kl) 52 43 34 25 16 : k=i+1 et l=j+2

    diagonale à 6 cases (ij) 50 41 32 23 14 05 : j de 0 à 5 et i=5-j
    diagonale à 6 cases (kl) 51 42 33 24 15 06 : k=i et l=j+1
    """
    # test des 2 diagonales croissantes à 4 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(4):
        i=3-j
        k=i+2
        l=j+3
        # teste la première diagonale [i][j] :
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        # teste la seconde diagonale [k][l] :
        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales croissantes à 5 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(5):
        i=4-j
        k=i+1
        l=j+2
        # teste la première diagonale [i][j] :
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        # teste la seconde diagonale [k][l] :
        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales croissantes à 6 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(6):
        i=5-j
        k=i
        l=j+1
        # teste la première diagonale [i][j] :
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        # teste la seconde diagonale [k][l] :
        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # teste les 6 diagonales décroissantes :
    """
    grille[i][j] (i=n° de la ligne de 0 à 5 et j=n° de la colonne de 0 à 6)

j :  0  1  2  3  4  5  6
    [X, X, X, X, 0, 0, 0] 0
    [X, X, X, X, X, 0, 0] 1
    [X, X, X, X, X, X, 0] 2
    [0, X, X, X, X, X, X] 3
    [0, 0, X, X, X, X, X] 4
    [0, 0, 0, X, X, X, X] 5
                          i

    Analyse du problème :
    Il y a :
        2 diagonales décroissantes à 4 cases (ij) : 03 14 25 36 et 20 31 42 53
        2 diagonales décroissantes à 5 cases (ij) : 02 13 24 35 46 et 10 21 32 43 54
        2 diagonales décroissantes à 6 cases (ij) : 01 12 23 34 45 56 et 00 11 22 33 44 55

    Dans les 6 cas j est croissant (analyse des diagonales de gauche à droite) et i est une fonction de j :
    diagonale à 4 cases (ij) 03 14 25 36 : j de 3 à 6 et i=j-3
    diagonale à 4 cases (ij) 20 31 42 53 : j de 0 à 3 et i=j+2

    diagonale à 5 cases (ij) 02 13 24 35 46 : j de 2 à 6 et i=j-2
    diagonale à 5 cases (ij) 10 21 32 43 54 : j de 0 à 4 et i=j+1

    diagonale à 6 cases (ij) 01 12 23 34 45 56 : j de 1 à 6 et i=j-1
    diagonale à 6 cases (ij) 00 11 22 33 44 55 : j de 0 à 5 et i=j

    Optimisons : le compteur de base est j, les 3 autres sont fonction de j :

    diagonale à 4 cases (ij) 03 14 25 36 : j de 3 à 6 et i=j-3
    diagonale à 4 cases (kl) 20 31 42 53 : k=j-1 et l=i

    diagonale à 5 cases (ij) 02 13 24 35 46 : j de 2 à 6 et i=j-2
    diagonale à 5 cases (kl) 10 21 32 43 54 : k=j-1 et l=i

    diagonale à 6 cases (ij) 01 12 23 34 45 56 : j de 1 à 6 et i=j-1
    diagonale à 6 cases (kl) 00 11 22 33 44 55 : k=i et l=i
    """
    # test des 2 diagonales décroissantes à 4 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(3,7):
        i=j-3
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0
    # test des 2 diagonales décroissantes à 5 cases :
    rouge=[0,0]
    bleu=[0,0]
    
    for j in range(2,7):
        i=j-2
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0
    # test des 2 diagonales décroissantes à 6 cases :
    rouge=[0,0]
    bleu=[0,0]

    for j in range(1,7):
        i=j-1
        k=i
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0
    # si on n'a rien trouvé on retourne 0 :
    return trouve

# La fonction tester_saisie demande au joueur de saisir un nombre entre 0 et 6,
# et réitère la demande tant que la valeur saisie n'est pas un entier dans cet intervale
def tester_saisie(joueur_courant):
    if joueur_courant==1:
        joueur='ROUGE'
    else:
        joueur='BLEU'
    saisie_correct=False
    # gestion des erreurs et filtrage des entrées : demande une saisie jusqu'à ce que la valeur entrée soit un chiffre entre 0 et 6
    # Les messages d'erreurs orientant l'utilisateur sont affichés sur la sortie standard (sans provoquer d'erreur)
    while not saisie_correct:
        s_colonne=input("%s : entrez la colonne où jouer (de 0 à 6) :" % joueur)
        # teste si la chaine saise est un entier :
        if not s_colonne.isdigit():
            print("Erreur de saise : la valeur entrée par le joueur %s n'est pas un nombre entier. Recommencez." % joueur)
        # teste si la valeur numérique est comprise entre 0 et 6 :
        elif int(s_colonne)<0 or int(s_colonne)>6:
            print("Erreur de saise : la valeur numérique entrée par le joueur %s n'est pas comprise entre 0 et 6. Recommencez." % joueur)
        else:
            saisie_correct=True
    # la chaine s_colonne est un chiffre entre 0 et 6 : on la convertit en entier et on la renvoie
    return int(s_colonne)

# La fonction jouer() demande au joueur courant dans quelle colonne (de 0 à 6) il veut jouer
def jouer(joueur_courant):
    if joueur_courant==1:
        joueur='ROUGE'
    else:
        joueur='BLEU'
    # La fonction tester_saisie renvoie forcément un chiffre entre 0 et 6 :
    colonne=tester_saisie(joueur_courant)
    while tab_colonne[colonne]==6:
        print('La colonne %d est pleine ! %s jouez dans une colonne non pleine' % (colonne,joueur))
        colonne=tester_saisie(joueur_courant)
    grille[5-tab_colonne[colonne]][colonne]=joueur_courant
    tab_colonne[colonne]+=1
    print('\nLe joueur %s vient de jouer dans la colonne %d :' % (joueur,colonne))


#############################################################################
#    P R O G R A M M E      P R I N C I P A L
#############################################################################
def jeu_puissance_4():
    print('Le nom des joueurs sera ici ROUGE et BLEU. Le joueur ROUGE commence.')
    print('Début de la partie (la grille est vide) :')
    gagnant=0
    while not grille_pleine() and gagnant==0:
        afficher_grille()
        jouer(joueur_courant)
        joueur_courant=3-joueur_courant
        gagnant=pions_alignes()
        if gagnant==1:
            print('Bravo ! Le joueur ROUGE a gagné !')
        elif gagnant==2:
            print('Bravo ! Le joueur BLEU a gagné !')
    afficher_grille()
    if gagnant==0:
        print("Fin de la partie : la grille est pleine et il n'y a pas 4 pions alignés")
    elif grille_pleine():
        print("Fin de la partie : 4 pions sont alignés et la grille est pleine")
    else:
        print("Fin de la partie : 4 pions sont alignés et la grille n'est pas pleine")

# ############################################################################
#    F I N     D U     P R O G R A M M E
# ############################################################################