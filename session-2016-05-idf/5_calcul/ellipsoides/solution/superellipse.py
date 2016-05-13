# coding: utf8
"""
implémentation d'une superellipse
"""

import numpy as np
from scipy.special import gamma
from pylab import *

from utils import spe_cos, spe_sin


class Superellipse(object):
    """
    définit une superellipse.

    x = rx c(theta, 2/m)
    y = ry s(theta, 2/m)

    où

    c(theta, m) = sign(cos(theta))|cos(theta)|**m
    s(theta, m) = sign(sin(theta))|sin(theta)|**m

    Paramètres
    ==========

    rx : rayon suivant x

    ry : rayon suivant y

    m : puissance dans l'expression de la superellipse.

    Attributs
    =========
    n : nombre de points de discrétisation en theta

    rx : rayon suivant x

    ry : rayon suivant y

    m : puissance dans l'expression de la superellipse.

    Méthodes
    ========

    cloud: renvoie les points de la surface.

    area: renvoie l'aire.

    """

    def __init__(self, rx, ry, m):
        self.rx = rx
        self.ry = ry
        self.m = m

    def cloud(self, n=10):
        """
        retourne les points à la surface de la superellipse

        Paramètre
        =========

        n : nombre de points de discrétisation en theta

        """
        theta = linspace(0., 2.*np.pi, n)
        x = self.rx*spe_cos(theta, 2./self.m)
        y = self.ry*spe_sin(theta, 2./self.m)
        return x, y

    


if __name__ == '__main__':
    se = Superellipse(1, 1, 2)
    x, y = se.cloud(12)
    plot(x,y, label = 'rx=%.1f, ry=%.1f, m=%.0f' % (se.rx, se.ry, se.m))
    se = Superellipse(2, 3, 3)
    x, y = se.cloud(12)
    plot(x,y, label = 'rx=%.1f, ry=%.1f, m=%.0f' % (se.rx, se.ry, se.m))
    legend(loc='best')
    title('superellipses')
    xlim([-3,3])
    ylim([-3,3])
    
    