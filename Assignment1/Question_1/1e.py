# Question (e): Calculate the vector normal to the plane defined by the points P1(5, 0, 0), P2(0, 0, 5), and P3(10, 0, 5).

import numpy as np

p1 = np.array([5,0,0])
p2 = np.array([0,0,5])
p3 = np.array([10,0,5])

N = np.cross((p3-p1),(p2-p1))

print('The Normal Vector to the plane is : ', N)