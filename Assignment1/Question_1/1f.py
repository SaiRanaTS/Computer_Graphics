#Question (f): Compute the area of the triangle defined by points P1(5, 0, 0), P2(0, 0, 5), and P3(10, 0, 5).

import numpy as np

p1 = np.array([5,0,0])
p2 = np.array([0,0,5])
p3 = np.array([10,0,5])

Area = 0.5*(np.linalg.norm(np.cross((p3-p1),(p2-p1))))
print('The area of the triangle is given by : ',Area )