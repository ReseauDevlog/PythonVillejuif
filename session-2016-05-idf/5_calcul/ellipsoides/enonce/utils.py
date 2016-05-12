# coding: utf8
"""
Fonctions utilisées dans la création des

- superellipses
- superellipsoides

"""

import math

def spe_cos(theta, m):
    """
    calcule sign(cos(theta))|cos(theta)|^m
    """
    cosw = math.cos(theta)
    return math.copysign(abs(cosw)**m, cosw)

def spe_sin(theta, m):
    """
    calcule sign(sin(theta))|sin(theta)|^m
    """
    sinw = math.sin(theta)
    return math.copysign(abs(sinw)**m, sinw)


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

