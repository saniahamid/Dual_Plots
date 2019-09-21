# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:40:29 2018

@author: hamid
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:12:25 2018

@author: sania
"""

from matplotlib import pyplot as plt
import numpy as np

ox1=[1,100,1.5,40,65] 
oy1=[2,15,60,20,45]
dx1=[80,70,25,0,10]
dy1=[90,30,30,0,80]
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
src1.append(list(np.asarray(ox1)+8000))
src1.append(list(np.asarray(oy1) ))

#destination 1a
des1a = []
des1a.append(list(np.asarray(dx1)+4000+8000))
des1a.append(list(np.asarray(dy1) ))

#dual 1a 
dual_fun(src1,des1a)
plt.scatter(dual[0],dual[1],color='#2d4059',label='dual 1a')
            
#source 2
src2 = []
src2.append(list(np.asarray(ox1) +11000))
src2.append(list(np.asarray(oy1) +200 ))

#destination 2a
des2a = []
des2a.append(list(np.asarray(dx1)+4000 +11000 ))
des2a.append(list(np.asarray(dy1)+ 200 ))

#dual 2a 
dual_fun(src2,des2a)
plt.scatter(dual[2],dual[3],color='#ffb400',label='dual 2a')
            
##source 3
#src3 = []
#src3.append(list(np.asarray(ox1) ))
#src3.append(list(np.asarray(oy1) ))
#
##destination 3a
#des3a = []
#des3a.append(list(np.asarray(dx1) + 4000))
#des3a.append(list(np.asarray(dy1)))
#
##dual 3a 
#dual_fun(src3,des3a)
#plt.scatter(dual[4],dual[5],color='#6a9c78',label='dual 3a')

#source 4
#src4 = []
#src4.append(list(np.asarray(ox1) ))
#src4.append(list(np.asarray(oy1) ))

#destination 4a
#des4a = []
#des4a.append(list(np.asarray(dx1) + 2828 ))
#des4a.append(list(np.asarray(dy1) + 2828))

#dual 4a 
#dual_fun(src4,des4a)
#plt.scatter(dual[6],dual[7],color='#90aeff',label='dual 4a')
     
plt.scatter(100,100)
plt.legend()
plt.grid()
plt.figure()
plt.show()

plt.scatter(4000,4000)
plt.scatter(src1[0],src1[1],color='#F5D76E',label='source 1')
plt.scatter(des1a[0],des1a[1],color='#F03434',label='destination 1')
plt.scatter(src2[0],src2[1],color='#00E640',label='source 2')
plt.scatter(des2a[0],des2a[1],color='#013243',label='destination 2a')
#plt.scatter(src3[0],src3[1],color='#6900ff',label='source 3')
#plt.scatter(des3a[0],des3a[1],color='#6a9c78',label='destination 3a')
#plt.scatter(src4[0],src4[1],color='#480032',label='source 4')
#plt.scatter(des4a[0],des4a[1],color='#ff8b6a',label='destination 4a')
#plt.scatter(200,10)
plt.legend(loc = 'best')
plt.grid()
#plt.figure()
plt.show()

