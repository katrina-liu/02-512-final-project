import numpy as np
from math import log

def variation_of_information(X, Y):
  n = max(float(X[-1][-1]),float(Y[-1][-1]))
  print(n)
  sigma = 0
  HC = 0
  HC_ = 0
  for x in X:
    p = float(int(float(x[1]))-int(float(x[0]))) / n
    # print(float(x[1]-x[0]))
    # print(int(float(x[1])))
    # print(int(float(x[0])))
    # print(n)
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