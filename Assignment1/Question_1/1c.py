import numpy as np

r = np.array([2,3,4])
s = np.array([5,6,7])

rs_sum = r+s
mag_rs = np.linalg.norm(rs_sum)

print('The addition of r and s gives a vector : ', rs_sum)
print('The maginitude of r + s is given by : ',mag_rs)

