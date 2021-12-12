import numpy as np
from math import log
import os
from os import listdir


#armatus
directory = 'src/HiCSeg_SpectralTAD_res/MCF7'

fnames = list(fname for fname in listdir(directory) )
fnames.sort()
fnames = fnames[1:]
print(fnames)
MCF7_pred = fnames
MCF10_pred = fnames

#truth
directory = 'data/GSE66733_Hi-C_MCF7_MCF10A_processed_HiCfiles_domains/TAD_boundaries'
fnames = list(fname for fname in listdir(directory) ) # if fname.endswith('.boundaries')
half_t = int(len(fnames)/2)
fnames.sort()
half_t = int(len(fnames)/2)
# print(fnames)
MCF10_truth = fnames[0:half_t - 1]
MCF7_truth = fnames[half_t:]



def variation_of_information(X, Y):
  n = max(float(X[-1][-1]),float(Y[-1][-1]))
  # print(n)
  sigma = 0
  HC = 0
  HC_ = 0
  for x in X:
    p = float(int(float(x[1]))-int(float(x[0]))) / n
    # print(p)
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



for i in range(len(MCF7_pred)):
  print(MCF7_pred[i])
  path = "src/HiCSeg_SpectralTAD_res/MCF10a/{fname}/hicseg_res.csv" #change 7 to 10a
  pred = []
  with open(path.format(fname = MCF7_pred[i]))as f:
    for line in f:
      start, end = line.strip().split(',')[2], line.strip().split(',')[3]
      pred.append([start, end])

  pred = pred[1:] #remove 'start, end'
  pred = pred[:-1] #remove last term that is a replicate
#   print(pred)
#   print(MCF7_pred[i])
  truth = []
  path = "data/GSE66733_Hi-C_MCF7_MCF10A_processed_HiCfiles_domains/TAD_boundaries/HiCStein-MCF10a-WT__hg19__{fname}__C-40000-iced.is1000000.ids240000.insulation.boundaries"
  with open(path.format(fname = MCF7_pred[i]))as f:
    for line in f:
      start, end = line.strip().split()[1], line.strip().split()[2]
      truth.append([start, end])
    #process so that range is similar
  truth = truth[1:] #remove 'start, end'

  truth = np.asarray(truth)
  truth = truth.astype(float)
  # print(pred, truth)
  VI = variation_of_information(pred, truth)
  print(VI)
      