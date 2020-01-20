import os
from rdm import Rdm

for subdir, dirs, files in os.walk('rdms'):
    if len(dirs) == 0 and len(files) != 0:
        analyser = Rdm(subdir)
        analyser.analyse()
