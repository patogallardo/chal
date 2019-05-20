import numpy as np
from chal import matrices


class Stack():
    def __init__(self, epsilons, ds, freqs):
        assert len(epsilons) == len(ds) + 2
        assert freqs.shape[0] > 1
        n_layers = len(ds)
        n_materials = len(epsilons)
        n_freq = len(freqs)

        self.n_layers = n_layers
        self.n_materials = n_materials
        self.n_freq = n_freq

        n_ls = [matrices.n(e_param) for e_param in epsilons]
        self.n_ls = n_ls
        Dls = []
        for j in range(n_materials):
            Dls.append(matrices.Dl(n_ls[j], n_freq))
        Pls = []
        for j in range(n_layers):
            Pls.append(matrices.Pl(ds[j], n_ls[j+1], freqs))
        self.Dls = Dls
        self.Pls = Pls
        self.getM()

    def getM(self):
        Dls = self.Dls
        Pls = self.Pls
        prod = np.linalg.inv(self.Dls[0])

        for j in range(self.n_layers):
            np.matmul(prod, Dls[j+1], out=prod)
            np.matmul(prod, Pls[j], out=prod)
            np.matmul(prod, np.linalg.inv(Dls[j+1]), out=prod)
        prod = np.matmul(prod, Dls[-1], out=prod)
        self.Ms = prod
        R = np.abs(self.Ms[:, 1, 0]/self.Ms[:, 0, 0])**2
        T = self.n_ls[-1]/self.n_ls[0] * np.abs(1./self.Ms[:, 0, 0])**2
        self.R = R
        self.T = T
