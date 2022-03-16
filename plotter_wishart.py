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
    
fileName = "wishart.dat"

data1 = np.loadtxt(fileName, usecols= [0], unpack = True)
data2 = np.loadtxt(fileName, usecols= [1],unpack = True)
data3= np.loadtxt(fileName, usecols= [2],unpack = True)
data4 = np.loadtxt(fileName, usecols= [3],unpack = True)


pylab.figure('1')
pylab.clf()
pylab.plot(xsteps,data1, label='wt')
pylab.plot(xsteps,data2, label='var3')
pylab.plot(xsteps,data3, label='var4')
pylab.plot(xsteps,data4, label='var8')
#pylab.title("S2 from backbone shifts", fontweight="bold")
pylab.ylabel("$\mathregular{S^2}$",fontweight="bold")
pylab.xlabel("residues", fontweight="bold")
pylab.legend(loc = 'upper rigth')
pylab.ylim(0,1)
pylab.savefig('s2_wishart.png', dpi = 600)

aver = 0
step = int(1)
for line in data4:
    #if step >= 20 and step <= 29 :
    aver += line
    step += 1
    
result = aver/37
print(result)

    