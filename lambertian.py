import math
import numpy as np
from scipy import interpolate
import random

"""
calculating generalized Lambertian radiant intensity model used to approximate the radiation pattern of light emitter
:param N: number of reflectances
:param m: mode number of the radiation lobe which specifies the directionality of the emitter == 1
"""
def calculate(N,m):

    AS1 = []
    Re = []
    p = []
    indices = []
    AS1prim = []
    AS = []
    AS2 = []

    for x in range(-90,91):
        AS1.append(x)

    for as1 in AS1:
        # generalized Lambertian radiation pattern
        Re.append(((m+1)/(2*math.pi))*math.pow(math.cos(math.radians(as1)),m))
  
    
    # array with fractions
    for re in Re:
        p.append(re/sum(Re))
 
    # reflectance distribution function, sum of all dimensions
    rdf = np.cumsum(p) 

    # unique values from an array with their indices
    rdf, indices = np.unique(rdf, return_index=True) 

    #onlu unique values
    for indice in indices:
        AS1prim.append(AS1[indice])

    #random value between 1 and N
    AS2 = np.random.uniform(0, 1, int(N))

    #interpolation function
    f = interpolate.interp1d(rdf, AS1prim)

    # using interpolation function on query points
    for query_points in AS2:
        AS.append(f(query_points))

    return AS


