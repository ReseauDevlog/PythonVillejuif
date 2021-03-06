# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:06:08 2016

@author: dmitry
"""




class Vecteur(object):
    def __init__(self, u=0, v=0, w=0):
        self.__x = u
        self.__y = v
        self.__z = w

    def __add__(self, other):
        if isinstance(other, Vecteur):
            newx = self.__x + other.__x
            newy = self.__y + other.__y
            return Vecteur(newx, newy)

    def __mul__(self, other):
        if isinstance(other, Vecteur):
          newx = self.__x * other.__x
          newy = self.__y * other.__y
          return Vecteur(newx, newy)

    def __getitem__(self, index):
        coords = [self.__x, self.__y, self.__z]
        return coords[index]


    def __str__(self):
        return "({:.0f},{:.0f},{:.0f})".\
           format(self.__x, self.__y, self.__z)


class Movement(object):
    def __init__(self, x=0, y=0, z=0, m=0):
        self._vitesse = Vecteur(x, y, z)
        self._masse = m


    def __str__(self):
        return "{}|{:d}".format(self._vitesse.__str__(), self._masse)


    def __eq__(self, other):
        return ( self._vitesse==other._vitesse ) and ( self._masse==other._masse )


class Impulsion(Movement):
    def __getitem__(self, index):
        return self._masse * self._vitesse[index]


class EnergieCinethique(Movement):
    def energie(self):
        E = 0
        for i in self._vitesse:
            E += i**2
        return 0.5 * self._masse * E

    def __str__(self):
        return super(EnergieCinethique, self).\
            __str__() +  ": energie Cinethieque = {}".\
            format(self.energie())


e = EnergieCinethique(12,22,2,5)
print (e)



"""





#v1 = Vecteur(8, 3)
#v2 = Vecteur(-1, 7)
#v3 = v1 * v2
#
#print(v3)

imp = Impulsion(12,22,2,5)

print(imp)

print ('Imp_z', imp[2] )

for i in imp:
    print (i)

"""