import numpy as np
from math import log
import os
from os import listdir


directory = 'src/results/'

fnames = list(fname for fname in listdir(directory) if fname.endswith('.consensus.txt'))
fnames.sort()
# print(fnames)
half = int(len(fnames)/2)
MCF7_pred = fnames[0:half - 1]
MCF10_pred = fnames[half:]

print(len(MCF7_pred))
print(len(MCF10_pred))
# # if the chromosome number is the same, append together
# MCF7_pred_final = []
# tmp = []
# for i in range(len(MCF7_pred)):
#   if i == 0:
#     prev = MCF7_pred[0] #.split('_')[4]
#     with open(path.format(fname = prev))as f:
#       for line in f:
#         start, end = line.strip().split()[1], line.strip().split()[2]
#         # start, end = start[-1], end[:-1]  
#         tmp.append([start, end])
#   else:
#     prev = MCF7_pred[i-1] #.split('_')[4]
#   #if same as prev, then
#   curr = MCF7_pred[i] #.split('_')
#   if curr != prev:
#     MCF7_pred_final.append(MCF7_pred[i].split('_')[4])
#     MCF7_pred_final.append(tmp)
#     tmp = []
#     path = "src/results/{fname}"
#     with open(path.format(fname = prev))as f:
#       for line in f:
#         start, end = line.strip().split()[1], line.strip().split()[2]
#         # start, end = start[-1], end[:-1]  
#         tmp.append([start, end])
#     # with open(path.format(fname = MCF7_pred[i]))as f:
#     # #add to tmp
#     print(tmp)
#   elif curr == prev:
#     print(MCF7_pred[i].split('_')[4])
#     path = "src/results/{fname}"
#     with open(path.format(fname = curr))as f:
#       for line in f:
#         start, end = line.strip().split()[1], line.strip().split()[2]
#         # start, end = start[-1], end[:-1]  
#         tmp.append([start, end])
  

    # with open("")as f:
    #process and append to tmp

#get the results

directory = 'data/GSE66733_Hi-C_MCF7_MCF10A_processed_HiCfiles_domains/TAD_boundaries'
fnames = list(fname for fname in listdir(directory) ) # if fname.endswith('.boundaries')
half_t = int(len(fnames)/2)
fnames.sort()
half_t = int(len(fnames)/2)
# print(fnames)
# even is 7, odd is 10
MCF10_truth = fnames[0:half_t - 1]
MCF7_truth = fnames[half_t:]
# print((MCF7_truth))

# print((MCF7_truth))
# print((MCF10_truth))

# print(len(MCF7_truth))


# print(MCF10_truth)
# print(len(fnames))
# print(MCF10)

def variation_of_information(X, Y):
  n = max(float(X[-1][-1]),float(Y[-1][-1]))
  print(n)
  sigma = 0
  HC = 0
  HC_ = 0
  for x in X:
    p = float(int(float(x[1]))-int(float(x[0]))) / n
    HC += -p *(log(p, 2))
    for y in Y:
      q =  float(int(float(y[1]))-int(float(y[0]))) / n
      tmp = range(max(int(float(x[0])), int(float(y[0]))), min(int(float(x[-1])), int(float(y[-1]))))
      tmp = len(tmp)
      r = float(tmp) / n
      if r > 0.0: #-r * (log(r / p, 2) + log(r / q, 2))
        sigma +=  r * (log(r / p*q, 2) )
  for y in Y:
    q =  float(int(float(y[1]))-int(float(y[0]))) / n
    HC_ += -q * (log(q, 2))
  return HC + HC_ - 2*sigma

# VI = variation_of_information(pred, truth)
# print(VI)

MCF7_results = []
MCF10_results = []

for i in range(len(MCF7_pred)):
# MCF7_pred[0] #.split('_')[4]
  path = "src/results/{fname}"
  pred = []
  with open(path.format(fname = MCF7_pred[i]))as f:
    for line in f:
      
      start, end = line.strip().split()[1], line.strip().split()[2]
      pred.append([start, end])
  truth = []
  path = "data/GSE66733_Hi-C_MCF7_MCF10A_processed_HiCfiles_domains/TAD_boundaries/{fname}"
  with open(path.format(fname = MCF7_truth[i]))as f:
    for line in f:
      start, end = line.strip().split()[1], line.strip().split()[2]
      truth.append([start, end])
    #process so that range is similar
    truth = truth[1:] #remove 'end'
  print(pred, truth)
      

for i in range(len(MCF10_pred)):
  path = "src/results/{fname}"
  with open(path.format(fname = MCF10_pred[i]))as f:
    for line in f:
      start, end = line.strip().split()[1], line.strip().split()[2]