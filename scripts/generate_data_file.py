import numpy as np
import os
import sys
from compute_time_interval import compute_time_interval

if __name__ == "__main__":
    """ 
    This script generates a data file in decimal from the input hex file from
    the machine
    Usage:
    python generate_data_file.py <infile> <outfile>
    """
    outFileName = sys.argv[2]
    data_dir_path = "../data/"
    outFileName = data_dir_path + outFileName
    if os.path.isfile(sys.argv[1]):
        file_handle = open(sys.argv[1], "r")
    else:
        print("Unable to locate file")
        sys.exit()
    times = []
    for line in file_handle.readlines():
        times.append(compute_time_interval(line.strip()))
    file_handle.close()
    np_times = np.array(times, dtype=np.float64)
    np.savetxt(outFileName, np_times, delimiter=',',
               header="time_interval (ns) ")
