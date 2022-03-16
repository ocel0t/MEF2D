# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:24:01 2018

@author: Nagy Tamás Milán

SCRIPT for making S2 plots
"""
import pylab as pylab
import numpy as np
import matplotlib.pyplot as mat

xsteps = [] 
for i in range(1,38):
    xsteps.append(i)
    

data1 = np.loadtxt("ss_wt_charmm36m.txt", usecols= [0], unpack = True)
data2 = np.loadtxt("ss_var3_charmm36m.txt", usecols= [0],unpack = True)
data3 = np.loadtxt("ss_var4_charmm36m.txt", usecols= [0],unpack = True)
data4 = np.loadtxt("ss_var8_charmm36m.txt", usecols= [0],unpack = True)

# =============================================================================
# data1 = np.ndarray.tolist(data1)
# data1 = data1[:3] + [None] + data1[3:]
# data2 = np.ndarray.tolist(data2)
# data2 = data2[:3] + [None] + data2[3:]
# data3 = np.ndarray.tolist(data3)
# data3 = data3[:3] + [None] + data3[3:]
# data4 = np.ndarray.tolist(data4)
# data4 = data4[:3] + [None] + data4[3:]
# =============================================================================

pylab.figure('1')
pylab.clf()
pylab.plot(xsteps,data1, label='wt (31%)')
pylab.plot(xsteps,data2, label='var3 (24%)')
pylab.plot(xsteps,data3, label='var4 (25%)')
pylab.plot(xsteps,data4, label='var8 (31%)')
pylab.title("Contribution of residues to bend conformers", fontweight="bold")
pylab.ylabel("fraction")
pylab.xlabel("residues")
pylab.legend(loc = 'upper left')
pylab.ylim(0,1)
pylab.savefig('ss_charmm36m.png', dpi = 600)

aver = 0
step = int(1)
for line in data4:
    #if step >= 20 and step <= 29 :
    aver += line
    step += 1
    
result = aver/37
print(result)

    