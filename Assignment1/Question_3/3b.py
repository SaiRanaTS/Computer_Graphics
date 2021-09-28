"""
Question(b): Does the ray intersect the triangle? If yes, what data would be put in the intersection record? If not,
why?
"""

import numpy as np

def intersection(a,b,c,O,D):
    t = (np.dot(np.cross((b-a),(c-a)) ,(a-O))) / (np.dot(np.cross((b-a),(c-a)),D))
    pz = O + t * D
    n = pz/np.linalg.norm(pz)
    print('Intersection Position is:',pz)
    print('Normal is : ', n)


a = np.array([2,0,0])
b = np.array([0,2,0])
c = np.array([0,0,2])

O = np.array([np.sqrt(3),np.sqrt(3),np.sqrt(3)])
D = np.array([-1/np.sqrt(3),-1/np.sqrt(3),-1/np.sqrt(3)])

intersection(a,b,c,O,D)