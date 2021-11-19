#!/usr/bin/env python

import subprocess
import sys
import os

from importlib import resources

def get_path(pdb):


    with resources.path("rigidipy.bin", "calc_rigidity_gcc4.8.4.bin") as f:
        data_file_path = f
    lib_location = os.path.dirname(data_file_path)
    print(lib_location)

    
    subprocess.call([data_file_path, pdb, lib_location])

   
def main():

    get_path(sys.argv[1])
    sys.exit(0)

      
if __name__ == "__main__":
    main()