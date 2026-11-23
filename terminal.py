import os
import config
def nettoyer_ecran() -> None:
    """
    Efface le contenu du terminal selon le système d'exploitation
    Préconditions : Aucune
    Postconditions : la console est nettoyée.
    """
    if os.name == "nt":
        os.system("cls")  # Pour Windows
    else:
        os.system("clear")  # Pour Mac et Linux

def afficher_menu()->None:
    """
    Affiche les options du menu principal.

    Préconditions: Aucune
    Postconditions : Les choix 1 à 5 sont affichés clairement à l'utilisateur.
    """
    print("SAE 1.02 - COMPARAISON D'ALGORITHMES DE TRI")
    print("  [1] Tri à bulles")
    print("  [2] Tri par insertion")
    print("  [3] Tri par fusion")
    print("  [4] Analyse des tris (Graphiques & Performances)")
    print("  [5] Quitter l'application\n")
    print("-" * 60)

def choixUtil(message: str, borne_min: int, borne_max: int) -> int:
    """
    Demande à l'utilisateur un entier compris entre borne_min et borne_max inclus.

    Préconditions :
        - message est une chaîne de caractères non vide.
        - borne_min <= borne_max.
    Postconditions :
        - Retourne un entier validé tel que borne_min <= resultat <= borne_max.
    """
    saisie_valide:bool
    valeur:int
    saisie_valide=False
    valeur=0
    while not saisie_valide:
        entree_utilisateur: str = input(message)
        try:
            valeur = int(entree_utilisateur)
            if borne_min <= valeur <= borne_max:
                saisie_valide = True
            else:
                print(config.couleur_erreur+"Erreur : entrez un nombre entre ", borne_min," et ", borne_max,""+config.COULEUR_RESET)
        except ValueError:
            print(config.couleur_erreur+"Erreur : ",entree_utilisateur,"n'est pas un entier valide."+config.COULEUR_RESET)

    return valeur
