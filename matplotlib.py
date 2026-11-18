from matplotlib import pyplot
x = [0,1,2,3,4,5]
y = [10,19,5,12,14,11]
pyplot.figure()  # Initialise la figure
pyplot.plot(x,y) # Réalise le tracé, x et y doivent ABSOLUMENT avoir la même taille
# Si x et y ne sont pas de même dimension, Python génère une erreur : x and y must have same first dimension
pyplot.show() #Affiche le graphique