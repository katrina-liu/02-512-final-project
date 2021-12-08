import subprocess
from os import listdir
import time

data_path = "../data/GSE66733_Hi-C_MCF7_MCF10A_processed_HiCfiles/40kb/"
gamma = 0.5
output_path = "results/"

def execute(gamma):
    for data_file in listdir(data_path):
        path = "".join([data_path,data_file])
        output = "".join([output_path,data_file])
        args = ("./armatus","-i", path, "-g", str(gamma), "-o", output, "-m")
        start = time.time()
        popen = subprocess.Popen(args,stdout=subprocess.PIPE)
        popen.wait()
        f = open("time.txt", "a")
        f.write("%s %f\n" % (data_file, time.time()-start))
        print(time.time()-start)
        output = popen.stdout.read()
        #print(output)
        print(output[str(output).find("user"):])

execute(gamma)

