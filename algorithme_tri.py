def triABulles(tailletableau,tableau):
    compteur=tailletableau
    estTrie=False
    while compteur>1 and not(estTrie):
        compteur-=1
        estTrie=True
        for secondcompteur in range(compteur):
            if tableau[secondcompteur+1][1]<tableau[secondcompteur][1]:
                variableintermediaire=tableau[secondcompteur+1]
                tableau[secondcompteur+1]=tableau[secondcompteur]
                tableau[secondcompteur]=variableintermediaire
                estTrie=False
    return tableau
a = [[1, 8, 5], [2, 4, 9], [3, 8, 1], [4, 2, 7]]
print(triABulles(4,a))

def triParInsertion(tailleTableau,Tableau):
    for compteur in range(1,tailleTableau):
        variableintermediaire=Tableau[compteur]
        secondcompteur=compteur
        while secondcompteur>0 and  Tableau[secondcompteur-1][1]>variableintermediaire[1]:
            Tableau[secondcompteur]=Tableau[secondcompteur-1]
            secondcompteur-=1
        Tableau[secondcompteur]=variableintermediaire
    return Tableau
print(triParInsertion(4,a)) 


def interClasserTableau(tableau1, tailletableau1, tableau2, tailletableau2):
    if tailletableau1 == 0:
        return tableau2
    elif tailletableau2 == 0:
        return tableau1
    elif tableau1[0] <= tableau2[0]:
        tableauIntermediaire = tableau1[1:]
        tailleTableauIntermediaire = tailletableau1 - 1
        return [tableau1[0]] + interClasserTableau(tableauIntermediaire, tailleTableauIntermediaire,tableau2, tailletableau2)
    else:
        tableauIntermediaire = tableau2[1:]
        tailleTableauIntermediaire = tailletableau2 - 1
        return [tableau2[0]] + interClasserTableau(tableau1, tailletableau1,tableauIntermediaire, tailleTableauIntermediaire)


def triParFusion(tailleTableau,Tableau):
    if tailleTableau <= 1:
        return Tableau
    else:
        tailletableau1 = tailleTableau // 2
        tailletableau2 = tailleTableau - tailleTableau // 2
        tableau1 = Tableau[:tailletableau1]
        tableau2 = Tableau[tailletableau1:]
        return interClasserTableau(triParInsertion(tailletableau1,tableau1), tailletableau1,triParInsertion(tailletableau2, tableau2), tailletableau2)

print(triParFusion(4,a))