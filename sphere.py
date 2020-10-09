"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

sphere.py
Proposito: Bears built with Raytracing
"""
from math_functions import *
from math import sqrt
from intersect import Intersect

#Circumference Object
class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, direction):
        L = sub(self.center, orig)
        tca = dot(L, direction)
        l = length(L)
        d2 = l ** 2 - tca ** 2
        if d2 > self.radius ** 2:
            return None
        thc = (self.radius ** 2 - d2) ** 1 / 2
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        hit = sum(orig, mul(direction, t0))
        normal = norm(sub(hit, self.center))
        return Intersect(
            distance=t0,
            point=hit,
            normal=normal
        ) 