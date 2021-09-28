import numpy as np

r = np.array([2,0,4])
s = np.array([5,6,10])

unit_r = r/np.linalg.norm(r)
unit_s = s/np.linalg.norm(s)

rs_dot = np.dot(unit_r,unit_s)

angle_btwn = round(np.degrees(np.arccos(rs_dot)),3)

print('The angle betrween the vectors is :', angle_btwn)