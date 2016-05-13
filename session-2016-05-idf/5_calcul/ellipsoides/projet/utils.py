# coding: utf8
"""
Fonctions utilisées dans la création des

- superellipses
- superellipsoides

"""

import numpy as np

def spe_cos(theta, m):
    """
    calcule sign(cos(theta))|cos(theta)|^m
    """
    cosw = np.cos(theta)
    return np.copysign(abs(cosw)**m, cosw)

def spe_sin(theta, m):
    """
    calcule sign(sin(theta))|sin(theta)|^m
    """
    sinw = np.sin(theta)
    return np.copysign(abs(sinw)**m, sinw)


def myformat(values):
    fe = ['{:+.1f}']*len(values)
    fg = '('+', '.join(fe)+')'
    return fg.format(*values)

def myformat2d(values):
    temp =  []
    for v in values:
        temp.append(myformat(v))
    fe = ['{}']*len(temp)
    fg = '('+', '.join(fe)+')'
    return fg.format(*temp)

