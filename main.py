import os
import sys
from rdm import Rdm

for subdir, dirs, files in os.walk(sys.argv[1]):
    if len(dirs) == 0 and len(files) != 0:
        analyser = Rdm(subdir)
        analyser.analyse()
