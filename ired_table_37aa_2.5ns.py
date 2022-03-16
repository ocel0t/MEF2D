# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:23:21 2018

@author: Nagy Tamás Milán

outputs in ired folder
"""

'''
Generating truncated trajectories (netcdf)

input = ired_2.5ns_prep.in
###

trajin MEF2D_full.netcdf

trajout Mef2D_full_1-250.netcdf netcdf onlyframes 1-250
trajout Mef2D_full_251-500.netcdf netcdf onlyframes 251-500
trajout Mef2D_full_501-750.netcdf netcdf onlyframes 501-750
trajout Mef2D_full_751-1000.netcdf netcdf onlyframes 751-1000
trajout Mef2D_full_1001-1250.netcdf netcdf onlyframes 1001-1250
trajout Mef2D_full_1251-1500.netcdf netcdf onlyframes 1251-1500
trajout Mef2D_full_1501-1750.netcdf netcdf onlyframes 1501-1750
trajout Mef2D_full_1751-2000.netcdf netcdf onlyframes 1751-2000
trajout Mef2D_full_2001-2250.netcdf netcdf onlyframes 2001-2250
trajout Mef2D_full_2251-2500.netcdf netcdf onlyframes 2251-2500
trajout Mef2D_full_2501-2750.netcdf netcdf onlyframes 2501-2750
trajout Mef2D_full_2751-3000.netcdf netcdf onlyframes 2751-3000
trajout Mef2D_full_3001-3250.netcdf netcdf onlyframes 3001-3250
trajout Mef2D_full_3251-3500.netcdf netcdf onlyframes 3251-3500
trajout Mef2D_full_3501-3750.netcdf netcdf onlyframes 3501-3750
trajout Mef2D_full_3751-4000.netcdf netcdf onlyframes 3751-4000
trajout Mef2D_full_4001-4250.netcdf netcdf onlyframes 4001-4250
trajout Mef2D_full_4251-4500.netcdf netcdf onlyframes 4251-4500
trajout Mef2D_full_4501-4750.netcdf netcdf onlyframes 4501-4750
trajout Mef2D_full_4751-5000.netcdf netcdf onlyframes 4751-5000
trajout Mef2D_full_5001-5250.netcdf netcdf onlyframes 5001-5250
trajout Mef2D_full_5251-5500.netcdf netcdf onlyframes 5251-5500
trajout Mef2D_full_5501-5750.netcdf netcdf onlyframes 5501-5750
trajout Mef2D_full_5751-6000.netcdf netcdf onlyframes 5751-6000
trajout Mef2D_full_6001-6250.netcdf netcdf onlyframes 6001-6250
trajout Mef2D_full_6251-6500.netcdf netcdf onlyframes 6251-6500
trajout Mef2D_full_6501-6750.netcdf netcdf onlyframes 6501-6750
trajout Mef2D_full_6751-7000.netcdf netcdf onlyframes 6751-7000
trajout Mef2D_full_7001-7250.netcdf netcdf onlyframes 7001-7250
trajout Mef2D_full_7251-7500.netcdf netcdf onlyframes 7251-7500
trajout Mef2D_full_7501-7750.netcdf netcdf onlyframes 7501-7750
trajout Mef2D_full_7751-8000.netcdf netcdf onlyframes 7751-8000
trajout Mef2D_full_8001-8250.netcdf netcdf onlyframes 8001-8250
trajout Mef2D_full_8251-8500.netcdf netcdf onlyframes 8251-8500
trajout Mef2D_full_8501-8750.netcdf netcdf onlyframes 8501-8750
trajout Mef2D_full_8751-9000.netcdf netcdf onlyframes 8751-9000
trajout Mef2D_full_9001-9250.netcdf netcdf onlyframes 9001-9250
trajout Mef2D_full_9251-9500.netcdf netcdf onlyframes 9251-9500
trajout Mef2D_full_9501-9750.netcdf netcdf onlyframes 9501-9750
trajout Mef2D_full_9751-10000.netcdf netcdf onlyframes 9751-10000
###

output = ired_2.5ns_prep.out
''' 

import os
os.system("mkdir ired2.5/")
os.system("cpptraj -p ../MEF2D.prmtop <ired_2.5ns_prep.in > ired_2.5ns_prep.out")

start = 1
end = 250

''' 
Generating IRED input files

output = ired"range".in

'''

for i in range(1,41): # 40 * 2.5 ns = 100 ns 
    trajin="Mef2D_full_" + str(start) + "-" + str(end) + ".netcdf"
    filename="ired2.5/ired" + str(start) + "-" + str(end) + ".in"
    file= open(filename, 'w')
    file.write("trajin " + str(trajin) + " netcdf") 
    file.write("\n")
    file.write("vector v2 :2@N ired :2@H\n"
               "vector v3 :3@N ired :3@H\n"
               "vector v4 :4@N ired :4@H\n"
               "vector v5 :6@N ired :6@H\n"
               "vector v6 :7@N ired :7@H\n"
               "vector v7 :8@N ired :8@H\n"
               "vector v8 :9@N ired :9@H\n"
               "vector v9 :10@N ired :10@H\n"
               "vector v10 :11@N ired :11@H\n"
               "vector v11 :12@N ired :12@H\n"
               "vector v12 :13@N ired :13@H\n"
               "vector v13 :14@N ired :14@H\n"
               "vector v14 :15@N ired :15@H\n"
               "vector v15 :16@N ired :16@H\n"
               "vector v16 :17@N ired :17@H\n"
               "vector v17 :18@N ired :18@H\n"
               "vector v18 :19@N ired :19@H\n"
               "vector v19 :20@N ired :20@H\n"
               "vector v20 :21@N ired :21@H\n"
               "vector v21 :22@N ired :22@H\n"
               "vector v22 :23@N ired :23@H\n"
               "vector v23 :24@N ired :24@H\n"
               "vector v24 :25@N ired :25@H\n"
               "vector v25 :26@N ired :26@H\n"
               "vector v26 :27@N ired :27@H\n"
               "vector v27 :28@N ired :28@H\n"
               "vector v28 :29@N ired :29@H\n"
               "vector v29 :30@N ired :30@H\n"
               "vector v30 :31@N ired :31@H\n"
               "vector v31 :32@N ired :32@H\n"
               "vector v32 :33@N ired :33@H\n"
               "vector v33 :34@N ired :34@H\n"
               "vector v34 :35@N ired :35@H\n"
               "vector v35 :36@N ired :36@H\n"
               "vector v36 :37@N ired :37@H\n"
               "vector v37 :38@N ired :38@H\n" )
    file.write("matrix ired name matired order 2\n"
                "diagmatrix matired vecs 36 out ired.vec name ired.vec\n"
                "ired relax NHdist 1.02 freq 500.0 tstep 100.0 tcorr 750.0 out v0.out noefile noe order 2 modes ired.vec orderparamfile " + "ired2.5/s2_" + str(start) + "-" + str(end) + ".dat\n")
    
    file.close()
    start += 250
    end += 250

start = str(1)
end = str(250)


'''
running cpptraj ired analysis

input = MEF2D.prmtop , ired"range".in
output = ired"range".out
data = ired"range".dat

'''

for i in range(1,41): ## !!!
    
    var = str("cpptraj -p ../MEF2D.prmtop <ired2.5/ired" + start + "-" + end + ".in > ired2.5/ired" + start + "-" + end + ".out")
    os.system(var)
    start = int(start)
    end = int(end)
    start += 250
    end += 250
    start = str(start)
    end = str(end)

'''
CALCULATION part
'''

import numpy as np
import sys, os
from glob import glob

store = {}
numRes = 36 # 37-Pro
fileResultRes = 1
fileResult= open("ired2.5/ired_result.out", 'w')
fileResult.write("### Average values of order parameters per residue ### \n")
fileResult.write(" \n")                


'''
creating list of .dat files of the working directory (all dat files!!!)
'''
name = "*.dat"
currDir = os.getcwd()
files_list = glob(os.path.join(currDir + "/ired2.5", name))

print("creating list of .dat files of the working directory...OK")

'''
creating dictionary with "len(files_list)" keys and 0 values 
NOT necessary
'''
#for i in range(1,len(files_list)): 
 #   store.update( {i:0} )

#print("creating dictionary with ""len(files_list)"" keys and 0 values...OK")


'''
reading data into dictionary
'''
key = 1
for i in files_list:
    var = np.loadtxt(i, skiprows=1, usecols=[1])
    store.update( { key : var } )
    key += 1

print("reading data into dictionary...OK")

'''
averaging S2 values of the residues
writing values to file
'''

for x in range(1,numRes+1): #numRES+1
    var2 = 0
    for i in range(1, len(store)+1):
        var2 += store[i][x-1]
    var2 /= len(store)
    fileResult.write(str(round(var2,3)) + "\n")

print("averaging S2 values of the residues...OK")
fileResult.close()  
print("writing values to file...OK")       
        
  
    

    