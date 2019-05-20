import numpy as np
from scipy import constants


def oneLayer(n, d, fs):
    '''Comptes transmission for a one layer model '''
    phi = n*2 * np.pi * fs * d/constants.c
    M11 = np.cos(phi) + 0.5j * np.sin(phi)*(n+1.0/n)
    T = np.abs(1.0/M11)**2
    return T
