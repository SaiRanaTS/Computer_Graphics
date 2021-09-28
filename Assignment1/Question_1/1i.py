import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-5,5,10)
a = 1
b = 1
c = -1

p_x = 1
p_y = 1

y = 1-x_values
x1 = np.array([1])
y1 = np.array([1])

plt.plot(y,'-r',label ='Line : x+y=1')
plt.scatter(x1,y1,label = 'Point: (1,1)')
plt.title('Line and Point Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()


plt.grid()
plt.show()

d = round(abs (a*p_x + b*p_y + c) / np.sqrt((a**2) + (b**2)),3)

print('The distance between the point and line is ',d)