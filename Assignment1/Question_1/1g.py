import numpy as np

# p1 + t(p1p2)

p1 = np.array([1,2,0])
p2 = np.array([3,1,5])

print('The implicit equation of the line is given by:\n')
print(p1,'+ t*',(p2-p1))

