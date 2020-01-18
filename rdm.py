import os
from scipy import io as sio
from scipy.spatial.distance import squareform
import numpy as np
from matplotlib import pyplot as pyplot

class Rdm:
  def __init__(self, file_name, arch):
    super().__init__()
    self.file_name = file_name
    self.arch = arch
    self.data = squareform(loadmat())
    self.mean = find_mean()
    self.std = find_std()

  def loadmat(self):
    return sio.loadmat(self.file_name)

  def find_mean(self):
    return np.mean(self.data)

  def find_std(self):
    return np.std(self.data)

  def analyse():
    min_idx = np.argpartition(self.data, 5)[:5]
    max_idx = np.argpartition(self.data, -5)[:5]

    min_data = self.data[min_idx]
    max_data = self.data[max_idx]

    min_std = (min_data - self.mean) // self.std
    max_std = (max_data - self.mean) // self.std

    results = open(self.arch + '.txt', 'a+')
    results.write('Least 5 values: \n')
    for val in min_std:
      results.write('The value {} lies in range {}σ and {}σ\n'.format(min_data[val], val, val + 1))
    results.write('Top 5 values: \n')
    for val in max_std:
      results.write('The value {} lies in range {}σ and {}σ\n'.format(max_data[val], val, val + 1))
    results.close()


