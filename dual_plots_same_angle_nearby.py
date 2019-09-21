# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 23:31:53 2018

@author: hamid
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
src1.append(list(np.asarray(ox1) - 1+150))
src1.append(list(np.asarray(oy1) - 2+150))

#destination 1a
des1a = []
des1a.append(list(np.asarray(dx1) + 92))
des1a.append(list(np.asarray(dy1) - 9.5))

#dual 1a 
dual_fun(src1,des1a)
plt.scatter(dual[0],dual[1],color='#ffa258',label='dual 1a')


#destination 1
des1 = []
des1.append(list(np.asarray(dx1) + 278+50))
des1.append(list(np.asarray(dy1) + 240.5+50))

#dual 1 
dual_fun(src1,des1)
plt.scatter(dual[2],dual[3],color='#a02a63',label='dual 1')

#destination 1e
des1e = []
des1e.append(list(np.asarray(dx1)- 8))
des1e.append(list(np.asarray(dy1)+90))

#source 2
src2 = []
src2.append(list(np.asarray(ox1) - 1+150))
src2.append(list(np.asarray(oy1) - 2+550))

#destination 2
des2 = []
des2.append(list(np.asarray(dx1) + 278+50))
des2.append(list(np.asarray(dy1) + 240.5+450))

#dual 2 
dual_fun(src2,des2)
plt.scatter(dual[4],dual[5],color='#6900ff',label='dual 2')

#source 3
src3 = []
src3.append(list(np.asarray(ox1) - 1+250+300))
src3.append(list(np.asarray(oy1) - 2+750+200))

#destination 3
des3 = []
des3.append(list(np.asarray(dx1) + 278+150+300))
des3.append(list(np.asarray(dy1) + 240.5+650+200))

#dual 3 
dual_fun(src3,des3)
plt.scatter(dual[6],dual[7],color='#cefc86',label='dual 3')

#source 4
src4 = []
src4.append(list(np.asarray(ox1) - 1+600))
src4.append(list(np.asarray(oy1) - 2+400))

#destination 4
des4 = []
des4.append(list(np.asarray(dx1) + 92+73.2+600))
des4.append(list(np.asarray(dy1) - 9.5+100+400))

#dual 3 
dual_fun(src4,des4)
plt.scatter(dual[8],dual[9],color='#6C7A89',label='dual 4')


plt.legend()
plt.grid()
plt.figure()
plt.show()

plt.scatter(src1[0],src1[1],color='#F89406',label='source 1')
plt.scatter(des1a[0],des1a[1],color='#F03434')
plt.scatter(des1[0],des1[1],color='#EC644B',label='destination 1')
plt.scatter(des1e[0],des1e[1],color='#E74C3C')
plt.scatter(src2[0],src2[1],color='#4ECDC4',label='source 2')
plt.scatter(des2[0],des2[1],color='#013243',label='destination 2')
plt.scatter(src3[0],src3[1],color='#663399',label='source 3')
plt.scatter(des3[0],des3[1],color='#DCC6E0',label='destination 3')
plt.scatter(src4[0],src4[1],color='#6900ff',label='source 4')
plt.scatter(des4[0],des4[1],color='#cefc86',label='destination 4')
plt.legend(loc = 'best')
plt.grid()
#plt.figure()
plt.show()