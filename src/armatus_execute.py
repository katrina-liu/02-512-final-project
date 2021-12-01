import subprocess
from os import listdir

data_path = "../data/"
gamma = 0.5
output_path = "results/"

def execute(gamma):
    for data_file in listdir(data_path):
        path = "".join([data_path,data_file])
        output = "".join([output_path,data_file])
        args = ("./armatus","-i", path, "-g", str(gamma), "-o", output, "-m")
        popen = subprocess.Popen(args,stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read()
        print(output)

execute(gamma)

