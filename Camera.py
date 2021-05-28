import numpy as np
import math

from User import User


class Matrix:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        if y < x:
            self.y = x
            self.x = y


class Camera:
    user = None

    def __init__(self, name, matrix_size, pixel_size, focal, work_time, weight):
        self.name = name
        self.matrix_size = matrix_size
        self.pixel_size = pixel_size * np.float_power(10, -6)
        self.spectral = ['R', 'G', 'B', 'NIR']
        self.focal = focal * np.float_power(10, -3)
        self.work_time = work_time
        self.weight = weight
        self.p = None
        self.q = None

    def getW(self):
        return self.user.GSD * self.focal / self.pixel_size

    def getLx(self):
        return self.matrix_size.x * self.user.GSD

    def getLy(self):
        return self.matrix_size.y * self.user.GSD

    def getBx(self):
        if self.p is None:
            self.p = self.user.p
        return self.getLx() * ((100 - self.p) / 100)

    def getBy(self):
        if self.q is None:
            self.q = self.user.q
        return self.getLy() * ((100 - self.q) / 100)

    def getHabs(self, Hmin, Hmax):
        return self.getW() + getHsr(Hmin, Hmax)

    def getRowNumber(self):
        Ny = self.user.Dy / self.getBy()
        if Ny < math.ceil(Ny):
            self.q = 100 - (100 * ((self.user.Dy / math.ceil(Ny)) / self.getLy()))
        return math.ceil(Ny)

    def getRowPhotosNumber(self):
        Nx = self.user.Dx / self.getBx() + 4
        if Nx < math.ceil(Nx):
            self.p = 100 - (100 * ((self.user.Dx / (math.ceil(Nx) - 4)) / self.getLx()))
        return math.ceil(Nx)

    def getPhotosNumber(self):
        return self.getRowPhotosNumber() * self.getRowNumber()


def getHsr(Hmin, Hmax):
    return (Hmin + Hmax) / 2


z_i = Camera("Z/I DMC IIe 230", Matrix(15552, 14144), 5.6, 92, 1.8, 63)
leica = Camera("Leica DMC III", Matrix(25728, 14592), 3.9, 92, 1.9, 63)
falcon = Camera("UltraCam Falcon M2 70", Matrix(17310, 11310), 6, 70, 1.35, 61)
eagle = Camera("UltraCam Eagle M2 80", Matrix(23010, 14790), 4.6, 80, 1.65, 61)