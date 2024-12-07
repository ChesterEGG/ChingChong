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