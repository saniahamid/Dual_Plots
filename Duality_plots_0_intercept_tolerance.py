# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:12:25 2018

@author: sania
"""

from matplotlib import pyplot as plt
import numpy as np

ox1=[1,1,1.5,2,3] 
oy1=[2,3,2.3,1.5,2]
dx1=[8,8.5,9,7.9,8]
dy1=[9,10,9.5,10,9.75]
dual = []

dd1 = 1
dd2 = 1
dd3 = 1
dd4 = 1
dd5 = 1

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
des1a.append(list(np.asarray(dx1) + 92+900))
des1a.append(list(np.asarray(dy1) - 9.5))

#dual 1a 
dual_fun(src1,des1a)
plt.scatter(dual[0],dual[1],color='#ff7517',label='dual 1a')
            
#source 2
src2 = []
src2.append(list(np.asarray(ox1) - 1+700))
src2.append(list(np.asarray(oy1) - 2))

#destination 2a
des2a = []
des2a.append(list(np.asarray(dx1) + 92+900+100))
des2a.append(list(np.asarray(dy1) - 9.5))

#dual 2a 
dual_fun(src2,des2a)
plt.scatter(dual[2],dual[3],color='#3e3939',label='dual 2a')

#source 3
src3 = []
src3.append(list(np.asarray(ox1) - 1+90))
src3.append(list(np.asarray(oy1) - 2))

#destination 3a
des3a = []
des3a.append(list(np.asarray(dx1) + 92+90))
des3a.append(list(np.asarray(dy1) - 9.5))

#dual 3a 
dual_fun(src3,des3a)
#plt.scatter(dual[4],dual[5],color='#6a9c78',label='dual 3a')
            
#source 4
src4 = []
src4.append(list(np.asarray(ox1) - 1+100))
src4.append(list(np.asarray(oy1) - 2))

#destination 4a
des4a = []
des4a.append(list(np.asarray(dx1) + 92+100))
des4a.append(list(np.asarray(dy1) - 9.5))

#dual 4a 
dual_fun(src4,des4a)
#plt.scatter(dual[6],dual[7],color='#90aeff',label='dual 4a')
            
plt.scatter(10,10)
plt.legend()
plt.grid()
plt.figure()
plt.show()

plt.scatter(src1[0],src1[1],color='#F89406',label='source 1')
plt.scatter(des1a[0],des1a[1],color='#F03434',label='destination 1a')
plt.scatter(src2[0],src2[1],color='#90aeff',label='source 2')
plt.scatter(des2a[0],des2a[1],color='#658525',label='destination 2a')
#plt.scatter(src3[0],src3[1],color='#6900ff',label='source 3')
#plt.scatter(des3a[0],des3a[1],color='#6a9c78',label='destination 3a')
#plt.scatter(src4[0],src4[1],color='#480032',label='source 4')
#plt.scatter(des4a[0],des4a[1],color='#ff8b6a',label='destination 4a')
plt.scatter(200,10)
plt.legend(loc = 'best')
plt.grid()
#plt.figure()
plt.show()