'''Matrix definitions go here'''
import numpy as np
from scipy import constants

def Dl(n_l, length):
    '''Defines D matrix from 5.1-23a'''
    res = np.empty([length, 2, 2], dtype=complex)
    res[:,0:2, 0:2] = np.array([[1.0, 1.0],[n_l, -n_l]],
                               dtype=complex)
    return res


def Pl(d, n_l, fs):
    '''Expects a vector containing the frequencies of interest.
    will generate an array of Pl matrices of [len(fs), 2, 2]
    following the definition in: 5.1-24'''
    length = len(fs)
    P = np.empty([length, 2, 2], dtype=complex)
    k = n_l * 2.0 * np.pi * f/constants.c
    #we write the elements explicitly, broadcasting will take care of the rest
    P[:, 0, 0] = np.exp(phi * 1.0)
    P[:, 0, 1] = np.zeros(length)
    P[:, 1, 0] = np.zeros(length)
    P[:, 1, 1] = np.exp(-phi*1.0j)
    return res


def n(e_params):
    '''Defines the index of refraction given real and imaginary parts of
    the dielectric constant.
    e_params = list of real and imaginary parts [1,0] for n=1.0'''
    if len(e_params)!=2:
        print "Wrong number of parameters for this model!!"
    e_prime, e_doublePrime = e_params
    n_l = np.sqrt(np.complex128(e_prime + e_doublePrime*1.0j)).conjugate()
    return n_l




