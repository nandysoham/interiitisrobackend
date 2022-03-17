import numpy as np
import json, codecs
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d




def fun(a):
  b=a.copy()
  for i in range(a.size):
    if i!=0 and i!=a.size-1:
      b[i]=(a[i-1]+a[i+1]+a[i])/3
    else:
      b[i]=a[i]
  return b


def returnable(): 
    data = fits.open('icdata.ic')

    Data = data[1].data


    d_new=fun(Data['RATE'].flatten())
    for i in range(100):
        d_new=fun(d_new)
    print(d_new)
    xitems = Data['Time'].tolist()
    yitems = d_new.tolist()
    return {"x" : xitems,  "y" : yitems}

if __name__ == "__main__":
    data = fits.open('icdata.ic')

    Data = data[1].data


    d_new=fun(Data['RATE'].flatten())
    for i in range(100):
        d_new=fun(d_new)
    
    plt.plot(Data['Time'],d_new)
    plt.show()