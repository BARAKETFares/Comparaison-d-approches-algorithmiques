import terminal
import config
def main()->None:
    choix:int
    continuer:bool
    continuer=True
    while continuer:
        terminal.nettoyer_ecran()
        terminal.afficher_menu()
        choix=terminal.choixUtil("Votre choix (1-5) : ",1,5)
        if choix==1:
            print(config.couleur_Info+"Lancement de Tri à bulles(en cours)")
        elif choix==2:
            print(config.couleur_Info+" Lancement du Tri par insertion (en cours de développement)..."+config.couleur_Reset)
            
        elif choix==3:
            print(config.couleur_Info+"Lancement du Tri par fusion (en cours de développement)..."+config.couleur_Reset)
        elif choix==4:
            print(config.couleur_Info+"Ouverture du module d'analyse (en cours de développement)..."+config.couleur_Reset)
        elif choix==5:
            continuer=False
            print("Fermeture de l'application . A bientot ! "+config.couleur_Reset)

if __name__=="__main__":
    main()