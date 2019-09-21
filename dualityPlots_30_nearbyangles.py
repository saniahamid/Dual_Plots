# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:47:47 2018

@author: sania
"""

from matplotlib import pyplot as plt
import numpy as np

ox1=[1,1,1.5,2,3] 
oy1=[2,3,2.3,1.5,2]
dx1=[8,8.5,9,7.9,8]
dy1=[9,10,9.5,10,9.75]
dual = []

def dual_fun( src , des ):
   a = []
   b1 = []
   b = []
   a = np.divide((np.asarray(des[1])-np.asarray(src[1])),(np.asarray(des[0])-np.asarray(src[0])))
   b1 = np.asarray(src[1])-np.multiply(np.asarray(src[0]),a)
   b = np.multiply(b1,-1)
   dual.append(a)
   dual.append(b)
   return

aa = 100
#source 1
src1 = []
src1.append(list(np.asarray(ox1) - 1+aa))
src1.append(list(np.asarray(oy1) - 2+aa))

#destination 1a 30degrees angle
des1a = []
des1a.append(list(np.asarray(dx1) + 92-13.4+aa))
des1a.append(list(np.asarray(dy1) - 9.5+50+aa))

#dual 1a 
dual_fun(src1,des1a)
plt.scatter(dual[0],dual[1],color='#6a9c78',label='dual 1a')
            
#destination 1b 35degrees angle
des1b = []
des1b.append(list(np.asarray(dx1) + 92-18.077+aa))
des1b.append(list(np.asarray(dy1) - 9.5+57.344+aa))

#dual 1b 
dual_fun(src1,des1b)
plt.scatter(dual[2],dual[3],color='#df0054',label='dual 1b')
            
#destination 1c 25degrees angle
des1c = []
des1c.append(list(np.asarray(dx1) + 92-9.54+aa))
des1c.append(list(np.asarray(dy1) - 9.5+42.24+aa))

#dual 1c 
dual_fun(src1,des1c)
plt.scatter(dual[4],dual[5],color='#90aeff',label='dual 1c')
            
#destination 1d 40degrees angle
des1d = []
des1d.append(list(np.asarray(dx1) + 92-23.372+aa))
des1d.append(list(np.asarray(dy1) - 9.5+64.29+aa))

#dual 1d 
dual_fun(src1,des1d)
plt.scatter(dual[6],dual[7],color='#ffd700',label='dual 1d')
            
plt.scatter(10,10)            
plt.legend()
plt.grid()
plt.figure()
plt.show()


plt.scatter(src1[0],src1[1],color='#F03434',label='source 1')
plt.scatter(des1a[0],des1a[1],color='#00E640',label='destination 1a')
plt.scatter(des1b[0],des1b[1],color='#91B496',label='destination 1b')
plt.scatter(des1c[0],des1c[1],color='#4ECDC4',label='destination 1c')
plt.scatter(des1d[0],des1d[1],color='#26A65B',label='destination 1d')
plt.legend(loc = 'best')
plt.grid()
#plt.figure()
plt.show()