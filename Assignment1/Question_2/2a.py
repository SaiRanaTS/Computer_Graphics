import numpy as np



def b_centric(x):
    Tri_area = 0.5 * np.linalg.norm((np.cross((p2 - p1), (p3 - p1))))
    Tri_beta = 0.5 * np.linalg.norm((np.cross((p1 - x), (p3 - x))))
    Tri_gama = 0.5 * np.linalg.norm((np.cross((p1 - x), (p2 - x))))
    beta1 = Tri_beta / Tri_area
    gama1 = Tri_gama / Tri_area
    alpha1 = 1 - beta1 - gama1
    print('Barycentric coordinates for point %s= [%.2f , %.2f , %.2f]\n' % (x, alpha1, beta1, gama1))



p1 = np.array([0,2,0])
p2 = np.array([0,0,4])
p3 = np.array([3,1,2])


pa = np.array([0,2,0])
pb = np.array([0,0,4])
pc = np.array([3,1,2])
pd = np.array([1,1,2])


b_centric(pa)
b_centric(pb)
b_centric(pc)
