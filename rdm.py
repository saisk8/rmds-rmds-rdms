import os
from scipy import io as sio
from scipy.spatial.distance import squareform
import numpy as np
from matplotlib import pyplot as pyplot

class Rdm:
  def __init__(self, file_name):
    super().__init__()
    self.file_name = file_name
    self.data = squareform(loadmat())

  def loadmat(self):
    return sio.loadmat(self.file_name)

  def find_mean(self):
    return np.mean(self.data)

  def find_std(self):
    return np.std(self.data)


