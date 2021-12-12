import numpy as np
from math import log
import os
from os import listdir


#armatus
directory = 'src/results/'

fnames = list(fname for fname in listdir(directory) if fname.endswith('.consensus.txt'))
fnames.sort()
# print(fnames)
half = int(len(fnames)/2)
MCF7_pred = fnames[0:half - 1]
MCF10_pred = fnames[half:]


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

def JI(pred, truth):
    count = 0
    intersection = len(list(set(pred).intersection(truth)))
    union = (len(pred) + len(truth)) - intersection
    return intersection / union

def variation_of_information(X, Y):
  n = max(float(X[-1][-1]),float(Y[-1][-1]))
  # print(n)
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

#armatus
MCF7_results = []
MCF10_results = []

for i in range(len(MCF10_pred)):
  print(MCF10_pred[i].split('_')[4])
  path = "src/results/{fname}"
  pred = []
  with open(path.format(fname = MCF7_pred[i]))as f:
    for line in f:
      start, end = line.strip().split()[1], line.strip().split()[2]
      pred.append([start, end])

  # print(MCF10_truth[i].split('_')[4])
  pred = np.asarray(pred)
  pred = pred.astype(float)
  pred = [[j*40000 for j in i] for i in pred]
  #JI
  
  pred_endpt = [row[1] for row in pred]
  pred_endpt = [i+1 for i in pred_endpt]
  # pred = np.asarray(pred)
  # for j in range(len(pred)):
  #     for k in range(len(pred[i])):
  #       pred[j][k] = pred[j][k] * 40000
  #       print(pred[j][k])
  truth = []
  path = "data/GSE66733_Hi-C_MCF7_MCF10A_processed_HiCfiles_domains/TAD_boundaries/{fname}"
  with open(path.format(fname = MCF10_truth[i]))as f:
    for line in f:
      start, end = line.strip().split()[1], line.strip().split()[2]
      truth.append([start, end])
    #process so that range is similar
  truth = truth[1:] #remove 'start, end'
  truth = np.asarray(truth)
  truth = truth.astype(float)
  truth_endpt = [row[1] for row in truth]
  # print(truth_endpt)
  # print(pred, truth)
  # VI = variation_of_information(pred, truth)
  # print(VI)
  # print(pred_endpt, truth_endpt)
  J_I = JI(pred_endpt, truth_endpt)
  print(J_I)
      

# for i in range(len(MCF10_pred)):
#   path = "src/results/{fname}"
#   with open(path.format(fname = MCF10_pred[i]))as f:
#     for line in f:
#       start, end = line.strip().split()[1], line.strip().split()[2]