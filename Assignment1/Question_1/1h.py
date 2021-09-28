import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(-6,6,100)

a1 = 2
b1 = 2
c1 = 4

a2 = 2
b2 = 4
c2 = 4

y1 = (c1/b1)-x_values*(a1/b1)
y2 = (c2/b2)-(x_values*(a2/b2))

plt.plot(x_values,y1,'-r',label = 'Line 1: 2x+2y=4')
plt.plot(x_values,y2,'-b',label = 'Line 2: 2x+4y=4')
plt.title('Line Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid()
plt.show()

m1 = -(b1/a1)
m2 = -(b2/a2)
angle = round(np.degrees(np.arctan(((m1-m2)/(1+(m1*m2))))),3)

print('The angle bewteen the lines is :',angle)
