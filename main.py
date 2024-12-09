import numpy as np
from algo.Dijkstra import Dijkstra
from algo.Bellman_Ford import Bellman_Ford
from algo.Floyd_Warshall import Floyd_Warshall

# Initiation des variables
INF = float('inf')
fichier_csv = 'graph/graphe.csv'

# Ouvrir et lire le fichier csv
with open(fichier_csv, 'r') as csv:
    # Lire les lignes
    lignes = csv.readlines()
    n = len(lignes)
    # Créer une matrice vide de taille n x n
    D = np.empty((n, n), dtype=float)

    # Diviser chaque ligne en une liste avec ses valeurs
    for i in range(n):
        ligne = lignes[i].split(',')
        # Remplacer dans la matrice vide les valeurs correspondantes aux index
        for j in range(n):
            D[i][j] = ligne[j]

    # Fermer le csv
    csv.close()

mat_dk = Dijkstra(D)
mat_bf = Bellman_Ford(D)
mat_fw = Floyd_Warshall(D)

# Vérifier si les 3 matrices sont égaux
assert np.array_equal(mat_dk, mat_bf) and np.array_equal(mat_dk, mat_fw)

# Imprimer la matrice coût
print("La matrice coût du graphe est:\n" + str(D) + "\n")
# Imprimer les 3 matrices distances des plus courts chemins avec chaque algo
print("La matrice des distances des plus courts chemins en utilisant l'algo de Dijkstra:\n" + str(mat_dk) + "\n")
print("La matrice des distances des plus courts chemins en utilisant l'algo de Bellman-Ford:\n" + str(mat_bf) + "\n")
print("La matrice des distances des plus courts chemins en utilisant l'algo de Floyd Warshall:\n" + str(mat_fw) + "\n")

