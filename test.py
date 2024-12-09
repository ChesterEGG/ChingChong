import numpy as np
from algo import Dijkstra

print("suce")

# Matrice coût
mat_cout = np.array([
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
assert np.array_equal(D, mat_cout)

test = np.matrix([
    [1, 3],
    [2, 4]
                  ])

test[0, 1] = 9

test2 = np.empty((len(test), len(test)), dtype=int)
test3 = [2] * 10

print(test[0, 0])
print(test2)
print(test3)