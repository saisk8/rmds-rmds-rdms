import os
from scipy import io as sio
from scipy.spatial.distance import squareform
import numpy as np
from matplotlib import pyplot as pyplot


class Rdm:
    def __init__(self, path):
        self.fpath = path
        self.file_name = os.path.join(self.fpath, 'submit_fmri.mat')
        self.data = squareform(self.loadmat(), force='tovector', checks=False)
        self.mean = self.find_mean()
        self.std = self.find_std()

    def loadmat(self):
        data = sio.loadmat(self.file_name)
        return data['EVC_RDMs']

    def find_mean(self):
        return np.mean(self.data)

    def find_std(self):
        return np.std(self.data)

    def analyse(self, k=5):
        min_idx = np.argpartition(self.data, k)[:k]
        max_idx = np.argpartition(self.data, -k)[-k:]

        min_data = self.data[min_idx]
        max_data = self.data[max_idx]

        min_std = (min_data - self.mean) // self.std
        max_std = (max_data - self.mean) // self.std

        path = os.path.join(self.fpath, 'analysis.txt')
        results = open(path, 'a+')
        results.write('Arch: {}, mean: {}, std: {}\n'.format(
            self.fpath.split('/')[-2], self.mean, self.std))
        results.write('Least 5 values: \n')
        for idx, val in enumerate(min_std):
            results.write('The value {} lies in range {}σ and {}σ\n'.format(
                min_data[idx], val, val + 1))
        results.write('Top 5 values: \n')
        for idx, val in enumerate(max_std):
            results.write('The value {} lies in range {}σ and {}σ\n'.format(
                max_data[idx], val, val + 1))
        results.close()
