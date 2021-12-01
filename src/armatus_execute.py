import subprocess

path = "../data/three-domains.txt.gz"
gamma = 0.5
output = "results/test"
args = ("./armatus","-i", path, "-g", str(gamma), "-o", output, "-m")
popen = subprocess.Popen(args,stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
print(output)