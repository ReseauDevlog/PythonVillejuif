


import math

# Une autre facon d'importer
from math import cos, sin

def linspace(begin, end, n):
    """
    Renvoie une liste de points espacés de manière régulière
    pour un intervalle donné.

    Paramètres
    ==========

    begin : borne inférieure de l'intervalle

    end : borne supérieure de l'intervalle

    n : nombre de points

    Sortie
    ======

    Renvoie la liste des points de discrétisation.

    """

    h = (end - begin)/(n-1)
    return [begin + i*h for i in range(n)]


def spe_cos(w, m):
    cosw = math.cos(w)
    return math.copysign(abs(cosw)**m, cosw)

def spe_sin(w, m):
    sinw = math.sin(w)
    return math.copysign(abs(sinw)**m, sinw)




def superellipse(n, rx, ry, m):
    """
    Renvoie les coordonnées de la superellipse.
    
    x = rx c(theta, 2/m)
    y = ry s(theta, 2/m)
    
    où
    
    c(theta, m) = sign(cos(theta))|cos(theta)|**m
    s(theta, m) = sign(sin(theta))|sin(theta)|**m
    
    Paramètres
    ==========
    
    n : nombre de points de discrétisation en theta
    
    rx : rayon suivant x
    
    ry : rayon suivant y
    
    m : puissance dans l'expression de la superellipse.
    
    Sortie
    ======
    
    les coordonnées de la superellipse.
    
    """    
    
    x, y = [], []
    for theta in linspace(0., 2.*math.pi, n):
        x.append(rx*spe_cos(theta, 2./m))
        y.append(ry*spe_sin(theta, 2./m))
    return x, y


def rotate_2D(X, Y, theta):
    Xr, Yr = [], []
    for x,y in zip(X,Y):
        Xr += [x*cos(theta)-y*sin(theta)]
        Yr += [x*sin(theta)+y*cos(theta)]
    return Xr, Yr




from pylab import *

x, y = superellipse(12, 2, 3, 2)

plot(x, y, label='superellipse(12, 2, 3, 2)')
theta = math.pi/2
x1, y1 = rotate_2D(x, y, theta) 
plot(x1, y1, label='rotated by %.1f'%theta)
legend(loc='best')

