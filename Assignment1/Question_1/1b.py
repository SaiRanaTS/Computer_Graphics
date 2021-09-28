import numpy as np

r = np.array([1,2,3])
mag_r = np.linalg.norm(r)
unit_r = r/mag_r

print('The Unit Vector for r  is :\n', unit_r)