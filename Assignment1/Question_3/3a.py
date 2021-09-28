"""
Consider a scene with a sphere and a triangle. The sphere’s center is at (0, 0, 0) and its radius is 1. The
triangle has vertices (2, 0, 0), (0, 2, 0), and (0, 0, 2). The camera (ray origin) is at (√3,√3,√3) and the ray
direction is (−√13,−√13,−√13).

Answer the following questions. The answers can be unreduced – they can be in terms of square roots,
fractions, and (inverse) trigonometric functions.

"""

"""
Question (a): Does the ray intersect the sphere? If yes, what data (position, normal, and t) would be put in the
intersection record? If not, why?
"""


import numpy as np


"""
Sphere = (P-C).(P-C)=Rˆ2
Ray = P(t) = O + t D
P = a point on sphere
C = Sphere center
R= Sphere radius
O = Origin of the ray
D = Direction of the ray
--------------------------------
(O+tD-C).(O+tD-C)=Rˆ2
tˆ2D.D +2tD.(O-C)+(O-C).(O-C)- Rˆ2 = 0
atˆ2 + bt + c = 0

a = D.D
b = 2.D.(O-C)
c = (O-C).(O-C)- Rˆ2
t =−b ± √(bˆ2 − 4 ac)/2a
"""

"""
b2−4ac is the discriminant. 
If, 
  discriminant < 0 : The ray dont touch nor intersect the sphere
  discriminant == 0 : The ray just touch the sphere
  discriminant > 0 : The ray dont touch nor intersect the sphere
"""



def evaluvation(c,r,d,o):  # Function for eveluvation of interaction and finding T1 and T2
    a = np.dot(d,d)
    b = 2 * np.dot(d,(o-c))
    c = (np.dot((o-c),(o-c))) - (r**2)
    delta = b**2 - (4*a*c)
    tp1 = round((-b + np.sqrt(delta)) / 2*a,2)
    tp2 = round((-b - np.sqrt(delta)) / 2*a,2)
    if delta > 0:
        print('The ray intersects the sphere in two points')
    elif delta == 0:
        print('The ray just touch the sphere')
    elif delta < 0:
        print('The ray dont touch nor intersect the sphere')
    return tp1, tp2


def intersection(C, R, D, O): #Function for finding interaction
    t1, t2 = evaluvation(C, R, D, O)
    Intersection_1 = O + (t1 * D)
    Intersection_2 = O + (t2 * D)
    normal_1 = Intersection_1 / np.linalg.norm(Intersection_1)
    normal_2 = Intersection_2 / np.linalg.norm(Intersection_2)
    print('Intersection Points are :\n', '1:', Intersection_1,'2:',Intersection_2)
    print('The normals are :\n','1:', normal_1,'2:',normal_2)
    print('The T : ', 't1 :', t1, 't2: ',t2)

    return Intersection_1, Intersection_2, normal_1, normal_2


C = np.array([0,0,0])
R = 1
D = np.array([-1/np.sqrt(3),-1/np.sqrt(3),-1/np.sqrt(3)])
O = np.array([np.sqrt(3),np.sqrt(3),np.sqrt(3)])

intersection(C, R, D, O)


