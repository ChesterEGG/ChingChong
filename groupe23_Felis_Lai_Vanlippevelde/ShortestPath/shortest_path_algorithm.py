import numpy as np

# Initiation de variable
INF = float('inf')

# Complexité de O(n^3), peut être amélioré
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
        # Distance au noeud lui-même = 0
        dist[noeud] = 0
        # Garde une trace des noeuds visités
        visited = [False] * n

        # Itérer sur tous les noeuds
        for _ in range(n):
            # Trouver le noeud non visité avec la plus petite distance
            min_distance = INF
            min_node = -1
            for i in range(n):
                if not visited[i] and dist[i] < min_distance:
                    min_distance = dist[i]
                    min_node = i

            # Si aucun noeud n'est accessible, arrêter
            if min_node == -1:
                break

            # Marquer ce noeud comme visité
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
        # Distance au noeud lui-même = 0
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