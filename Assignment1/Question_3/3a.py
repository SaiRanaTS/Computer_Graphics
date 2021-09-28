import numpy as np


def evaluvation(c,r,d,o):
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
        print("The ray dont touch nor intersect the sphere")
    return tp1, tp2


def intersection(C, R, D, O):
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


