#!/usr/bin/env python

import subprocess
import sys
import os

from importlib import resources
from sys import platform

def get_path(pdb):
    if platform == "linux" or platform == "linux2":
        with resources.path("rigidipy.bin", "calc_rigidity_gcc4.8.4.bin") as f:
            data_file_path = f
    elif platform == "darwin":
        with resources.path("rigidipy.bin", "calc_rigidity_OSX.bin") as f:
            data_file_path = f
    elif platform == "win32":
        print('ANSURR will not yet run on Windows')
        sys.exit(0)

    lib_location = os.path.dirname(data_file_path)
    subprocess.call([data_file_path, pdb, lib_location])
   
def main():

    get_path(sys.argv[1])
    sys.exit(0)

      
if __name__ == "__main__":
    main()