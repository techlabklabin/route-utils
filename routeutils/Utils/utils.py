import geopy.distance
from math import degrees
import numpy as np

def makeNewPoint(geoJsonPoint):
    return (geoJsonPoint[1], geoJsonPoint[0])

def makeVector(pointA, pointB):
    return [pointB[0] - pointA[0], pointB[1] - pointA[1]]

def distanceMeteres(point1, point2):
    return geopy.distance.geodesic(point1, point2).km * 1000

def angleBetweenVectors(vector1, vector2):
    unit_vector_1 = vector1 / np.linalg.norm(vector1)
    unit_vector_2 = vector2 / np.linalg.norm(vector2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    angleDegress = degrees(angle)
    
    return angleDegress
