import numpy as np
from algo import Dijkstra

print("suce")
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