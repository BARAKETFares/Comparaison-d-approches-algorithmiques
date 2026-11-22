def triABulles(tableau,tailletableau):
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
print(triABulles(a,4))