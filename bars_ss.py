# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:22:11 2019

@author: Nagy Tamás Milán
"""

# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.21

# set height of bar


wt = np.loadtxt("ss_wt_charmm36m.txt", usecols= [0], unpack = True)
var3 = np.loadtxt("ss_var3_charmm36m.txt", usecols= [0],unpack = True)
var4 = np.loadtxt("ss_var4_charmm36m.txt", usecols= [0],unpack = True)
var8 = np.loadtxt("ss_var8_charmm36m.txt", usecols= [0],unpack = True)

# Set position of bar on X axis
r1 = np.arange(len(wt))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

# Make the plot
plt.bar(r1, wt, width=barWidth, edgecolor='black', label='wt (unclustered = 16%)')
plt.bar(r2, var3, width=barWidth, edgecolor='black', label='var3 (unclustered = 13%) ')
plt.bar(r3, var4, width=barWidth, edgecolor='black', label='var4 (unclustered = 25%)')
plt.bar(r4, var8, width=barWidth, edgecolor='black', label='var8 (unclustered = 29%)')        

# Add xticks on the middle of the group bars
plt.title('Comparing population of similar conformers: ff14SBonlysc')
plt.xlabel('clusters', fontweight='bold')
plt.ylabel('no. of conformers', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(wt))], ['1', '2', '3', '4', '5'])


# Create legend & Show graphic
plt.legend()
plt.savefig('clusters_charmm36m.png', dpi=600)
plt.show()
