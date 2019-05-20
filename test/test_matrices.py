from chal import matrices
import numpy as np


def test_Dl():
    length = 3
    n_l = 3.4
    Dl = matrices.Dl(n_l, length)
    assert Dl.shape == (length, 2, 2)


def test_Pl():
    d = 1e-3
    n_l = 3.4
    length = 3
    fs = np.linspace(150e9, 300e9, length)
    Pl = matrices.Pl(d, n_l, fs)
    assert Pl.shape == (length, 2, 2)
    assert Pl[0, 0, 1] == 0
    assert Pl[0, 1, 0] == 0
