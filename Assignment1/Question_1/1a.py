import numpy as np


p = np.array([4,5,6])
mag = round(np.linalg.norm(p),3)

print('The given position vector  is : ', p[0],p[1],p[2])
print('The magnitude of the given position vector is : ', mag)


