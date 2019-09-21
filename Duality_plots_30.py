# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:47:02 2018

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

#source 1
src1 = []
src1.append(list(np.asarray(ox1) - 1))
src1.append(list(np.asarray(oy1) - 2))

#destination 1a
des1a = []
des1a.append(list(np.asarray(dx1) + 92-13.4))
des1a.append(list(np.asarray(dy1) - 9.5+50))

#dual 1a 
dual_fun(src1,des1a)
plt.scatter(dual[0],dual[1],color='#6a9c78',label='dual 1a')
            
#destination 1b
des1b = []
des1b.append(list(np.asarray(dx1) + 92+73.2))
des1b.append(list(np.asarray(dy1) - 9.5+100))

#dual 1b 
dual_fun(src1,des1b)
plt.scatter(dual[2],dual[3],color='#480032',label='dual 1b')
            
#destination 1c
des1c = []
des1c.append(list(np.asarray(dx1) + 92+419.6))
des1c.append(list(np.asarray(dy1) - 9.5+300))

#dual 1c 
dual_fun(src1,des1c)
plt.scatter(dual[4],dual[5],color='#ff8b6a',label='dual 1c')
            
#source 2
src2 = []
src2.append(list(np.asarray(ox1) - 1+400))
src2.append(list(np.asarray(oy1) - 2+150))

#destination 2a
des2a = []
des2a.append(list(np.asarray(dx1) + 92+419.6+400))
des2a.append(list(np.asarray(dy1) - 9.5+300+150))

#dual 2a 
dual_fun(src2,des2a)
plt.scatter(dual[6],dual[7],color='#00454a',label='dual 2a')


plt.scatter(10,10)            
plt.legend()
plt.grid()
plt.figure()
plt.show()


plt.scatter(src1[0],src1[1],color='#F03434',label='source 1')
plt.scatter(des1a[0],des1a[1],color='#00E640',label='destination 1a')
plt.scatter(des1b[0],des1b[1],color='#91B496',label='destination 1b')
plt.scatter(des1c[0],des1c[1],color='#4ECDC4',label='destination 1c')
plt.scatter(src2[0],src2[1],color='#DB0A5B',label='source 2')
plt.scatter(des2a[0],des2a[1],color='#26A65B',label='destination 2a')
plt.legend(loc = 'best')
plt.grid()
#plt.figure()
plt.show()