import math
import numpy as np
from scipy import interpolate
import random

def calculate(N,m):

    AS1 = []
    Rs = []
    p = []
    indices = []
    AS1prim = []
    AS = []
    AS2 = []
    for x in range(-90,91):
        AS1.append(x)

    for degrees in AS1:
        Rs.append(math.pow(((m+1)/(2*math.pi))*math.cos(math.radians(degrees)),m))
       
    for rs in Rs:
        p.append(rs/sum(Rs))
 
    rdf = np.cumsum(p) # sum of all dimensions
    rdf, indices = np.unique(rdf, return_index=True) # unique values from an array

    for indice in indices:
        AS1prim.append(AS1[indice])

    AS2 = np.random.uniform(0, 1, int(N))

    f = interpolate.interp1d(rdf, AS1prim)

    for points in AS2:
        AS.append(f(points))

    return AS


