import morpion
import puissance4
import pickle
import scores

#choix présent sur le menu
menu_options = {
    1: 'devinettes',
    2: 'allumettes',
    3: 'morpion',
    4: 'puissance 4',
    5: 'regles',
    6: 'exit'
}


#imprimer le menu
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


if __name__=='__main__':
    choice : str #définition du type de toutes les variables
    player1 : str
    score_all : list[list[str]]
    score_mor : list[list[str]]
    score_dev : list[list[str]]
    player2 : str
    endallum : list[str]
    enddevine : list[str]
    endmorpion : list[str]
    score_dev = []
    score_all = []
    score_mor = []
    with open('./sauvegarde/endall.pkl', 'wb') as fp:
        pickle.dump(score_all, fp)

    with open('./sauvegarde/endmor.pkl', 'wb') as fp:
        pickle.dump(score_mor, fp)
    
    with open('./sauvegarde/enddev.pkl', 'wb') as fp:
        pickle.dump(score_dev, fp)

    with open("./sauvegarde/endall.pkl","rb") as fsal : 
        score_all = pickle.load(fsal)
    with open("./sauvegarde/endmor.pkl","rb") as fmorp : 
        score_mor = pickle.load(fmorp)
    with open("./sauvegarde/enddev.pkl","rb") as fdev : 
        score_dev = pickle.load(fdev)
    
    #initialisation des variables
    endallum = []
    enddevine = []
    endmorpion = []

    print(score_mor)

    #imprimerle menu en boucle tant que les joueurs ne choisissent pas de sortir du programme
    while(True):
        #titre
        print(r"""                                           
                                   (          
          )   (       (           ))\ )   (   
 `  )  ( /(  ))\ (   ))\    (  ( /(()/(  ))\  
 /(/(  )(_))/((_))\ /((_)   )\ )(_))(_))/((_) 
((_)_\((_)_(_))(((_|_))    ((_|(_)(_) _(_))   
| '_ \) _` | || (_-< -_)  / _|/ _` |  _/ -_)  
| .__/\__,_|\_,_/__|___|  \__|\__,_|_| \___|  
|_|                                          
              """)

        print_menu()
        #Lancement du menu et des procédures correspondantes aux différentes parties du programmes
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check quel choix est entré et s'il correspond à un choix présent
        if option == 1:
           print("devinettes")

        elif option == 2:  
            print("allumettes")

        elif option == 3:
            player1 = input("entrer le pseudo du joueur 1 :")
            player2 = input("entrer le pseudo du joueur 2 :")
            endmorpion = morpion.jeu_du_morpion(player1,player2)
            scores.addToScore(endmorpion[0],endmorpion[1],score_mor)
            scores.afficheTableauScores(score_mor)
            scores.triescores(score_mor)
            
        elif option == 4:
            puissance4.jeu_puissance_4()

        elif option == 5:
            print("règles")

        elif option == 6:
            print("Au revoir")
            exit()
        else:
            print('choix inexistant merci de rentrer un nombre entre 1 et 6 compris.')
    
    print("lancement")
    with open("./sauvegarde/scoredev.pkl", "rb") as fsdev :
        pickle.dump(score_dev, fsdev)
    with open("./sauvegarde/scoreal.pkl", "rb") as fsal :
        pickle.dump(score_all, fsal)
    with open("./sauvegarde/scoremmor.pkl", "rb") as fsmor :
        pickle.dump(score_mor, fsmor)