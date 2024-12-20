import numpy as np

# Initiation des variables
INF = float('inf')


def Floyd_Warshall(C):
    """
        Calcule la matrice de distance des plus courts chemins entre toutes les paires de noeuds d’un graphe en utilisant
        l'algorithme de Floyd-Warshall.

        input: C --> une matrice numpy n x n de coût C
        output: Une matrice n × n contenant les distances des plus courts chemins
                entre toutes les paires de noeuds d'un graphe.
    """
    # Nombre de noeuds
    n = len(C)
    # Copier la matrice coût sur D
    D = C.copy()

    for k in range(n):  # Sommet intermédiaire
        for i in range(n):  # Sommet source
            for j in range(n):  # Sommet destination
                # Mise à jour de la distance minimale
                if D[i][k] != INF and D[k][j] != INF:  # Éviter les additions avec des INF
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    return D

