import os
from rdm import Rdm


for subdir, dirs, files in os.walk('rdms'):
  if len(dirs) == 0 and len(files) != 0:
    # print(files)
    # Get the architecture, image set
    # Construct the object and call analyse method
