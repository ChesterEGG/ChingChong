import numpy
import numpy as np

# Initiation de variable
INF = float('inf')

# Complxité de O(n^3), peut être améliorer
def Dijkstra(C):
    """
    Calcule la matrice de distance des plus courts chemins entre toutes les paires de noeuds d’un graphe en utilisant
    l'algorithme de Dijkstra.

    input: C --> une matrice numpy n x n de coût C
    output: Une matrice n × n contenant les distances des plus courts chemins 
            entre toutes les paires de noeuds d'un graphe.
    """
    # Nombre de noeud
    n = len(C)
    # Création d'une matrice de taille n x n vide
    D = np.empty((n, n), dtype=float)

    def chemins_plus_court(noeud):
        """
        Calcule les plus chemins le plus court d'un noeud

        Input: noeud --> un int qui représente l'index un noeud du graphe
        Output: Une liste de int avec la valeur des plus courtes distances du noeud
        """
        # Initialisation des distances à l'infini
        dist = [INF] * n
        # Distance au nœud lui-même = 0
        dist[noeud] = 0
        # Garde une trace des nœuds visités
        visited = [False] * n

        # Itérer sur tous les nœuds
        for _ in range(n):
            # Trouver le nœud non visité avec la plus petite distance
            min_distance = INF
            min_node = -1
            for i in range(n):
                if not visited[i] and dist[i] < min_distance:
                    min_distance = dist[i]
                    min_node = i

            # Si aucun nœud n'est accessible, arrêter
            if min_node == -1:
                break

            # Marquer ce nœud comme visité
            visited[min_node] = True

            # Mettre à jour les distances pour les voisins
            for voisin in range(n):
                if C[min_node][voisin] != INF and not visited[voisin]:
                    new_dist = dist[min_node] + C[min_node][voisin]
                    if new_dist < dist[voisin]:
                        dist[voisin] = new_dist

        return dist

    # Appliquer Dijkstra pour chaque noeud comme source
    for i in range(n):
        D[i] = chemins_plus_court(i)

    return D


C = np.array([
    # A    B    C    D    E    F    G    H    I    J
    [0,   4,   4,   3,   INF, INF, INF, INF, INF, INF],  # A
    [4,   0,   1,   INF, 3,   INF, 4,   INF, INF, INF],  # B
    [4,   1,   0,   3,   3,   INF, INF, INF, INF, INF],  # C
    [3,   INF, 3,   0,   INF, 4,   INF, INF, 5,   INF],  # D
    [INF, 3,   3,   INF, 0,   5,   5,   3,   INF, INF],  # E
    [INF, INF, INF, 4,   5,   0,   INF, 4,   4,   5],    # F
    [INF, 4,   INF, INF, 5,   INF, 0,   3,   INF, INF],  # G
    [INF, INF, INF, INF, 3,   4,   3,   0,   INF, 5],    # H
    [INF, INF, INF, 5,   INF, 4,   INF, INF, 0,   5],    # I
    [INF, INF, INF, INF, INF, 5,   INF, 5,   5,   0]     # J
])
print(Dijkstra(C))