import numpy as np

# Initiation des variables
INF = float('inf')


def Bellman_Ford(C):
    """
    Calcule la matrice de distance des plus courts chemins entre toutes les paires de noeuds d’un graphe en utilisant
    l'algorithme de Bellman-Ford.

    input: C --> une matrice numpy n x n de coût C
    output: Une matrice n × n contenant les distances des plus courts chemins
            entre toutes les paires de noeuds d'un graphe.
    """

    # Nombre de noeuds
    n = len(C)
    # Création d'une matrice de taille n x n vide
    D = np.empty((n, n), dtype=float)

    def chemin_plus_court(noeud):
        """
        Calcule les plus chemins le plus court d'un noeud

        Input: noeud --> un int qui représente l'index un noeud du graphe
        Output: Une liste de int avec la valeur des plus courtes distances du noeud
        """
        # Initialisation des distances à l'infini
        dist = [INF] * n
        # Distance au nœud lui-même = 0
        dist[noeud] = 0

        # Appliquer |V| - 1 relaxations pour toutes les arêtes
        for _ in range(n - 1):
            for i in range(n):
                for j in range(n):
                    if C[i, j] != INF and dist[i] + C[i, j] < dist[j]:
                        dist[j] = dist[i] + C[i, j]
        return dist

    # Appliquer Bellman-Ford pour chaque noeud comme source
    for i in range(n):
        D[i] = chemin_plus_court(i)

    return D

