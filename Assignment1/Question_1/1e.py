import numpy as np

p1 = np.array([5,0,0])
p2 = np.array([0,0,5])
p3 = np.array([10,0,5])

N = np.cross((p3-p1),(p2-p1))

print('The Normal Vector to the plane is : ', N)