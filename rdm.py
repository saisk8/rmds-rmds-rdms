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

  def plot(self):
    # the data points
    plt.scatter(x, self.data)
    # the mean
    plt.plot(self.mean, self.mean)
    # save plot
    plt.savefig(self.arch)

