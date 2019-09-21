# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 14:51:46 2018

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
des1a.append(list(np.asarray(dx1) + 92))
des1a.append(list(np.asarray(dy1) - 9.5))

#dual 1a 
dual_fun(src1,des1a)
if dd1 == 1:
    plt.scatter(dual[0],dual[1],color='#ffa258',label='dual 1a')

#destination 1b
des1b = []
des1b.append(list(np.asarray(dx1) + 78))
des1b.append(list(np.asarray(dy1) + 40.5))

#dual 1b 
dual_fun(src1,des1b)
if dd1 == 1:
    plt.scatter(dual[2],dual[3],color='#a02a63',label='dual 1b')

#destination 1c
des1c = []
des1c.append(list(np.asarray(dx1) + 60))
des1c.append(list(np.asarray(dy1) + 58.5))

#dual 1c 
dual_fun(src1,des1c)
if dd1 == 1:
    plt.scatter(dual[4],dual[5],color='#003545',label='dual 1c')

#destination 1d
des1d = []
des1d.append(list(np.asarray(dx1) + 42))
des1d.append(list(np.asarray(dy1) + 74.5))

#dual 1d 
dual_fun(src1,des1d)
if dd1 == 1:
    plt.scatter(dual[6],dual[7],color='#90aeff',label='dual 1d')

#destination 1e
des1e = []
des1e.append(list(np.asarray(dx1)- 8))
des1e.append(list(np.asarray(dy1)+90))


#source 2
src2 = []
src2.append(list(np.asarray(ox1) + 199))
src2.append(list(np.asarray(oy1) - 2))

#destination 2a
des2a = []
des2a.append(list(np.asarray(dx1) + 291))
des2a.append(list(np.asarray(dy1) - 9.5))

#dual 2a 
dual_fun(src2,des2a)
if dd2 == 1:
    plt.scatter(dual[8],dual[9],color='#6900ff',label='dual 2a')

#destination 2b
des2b = []
des2b.append(list(np.asarray(dx1) + 277))
des2b.append(list(np.asarray(dy1) + 40.5))

#dual 2b 
dual_fun(src2,des2b)
if dd2 == 1:
    plt.scatter(dual[10],dual[11],color='#cefc86',label='dual 2b')

#destination 2c
des2c = []
des2c.append(list(np.asarray(dx1) + 260))
des2c.append(list(np.asarray(dy1) + 58.5))

#dual 2c 
dual_fun(src2,des2c)
if dd2 == 1:
    plt.scatter(dual[12],dual[13],color='#df0054',label='dual 2c')

#destination 2d
des2d = []
des2d.append(list(np.asarray(dx1) + 242))
des2d.append(list(np.asarray(dy1) + 74.5))

#dual 2d 
dual_fun(src2,des2d)
if dd2 == 1:
    plt.scatter(dual[14],dual[15],color='#ffd700',label='dual 2d')

#destination 2e
des2e = []
des2e.append(list(np.asarray(dx1)+ 192))
des2e.append(list(np.asarray(dy1)+90))

#source 3
src3 = []
src3.append(list(np.asarray(ox1) - 1))
src3.append(list(np.asarray(oy1) + 198))

#destination 3a
des3a = []
des3a.append(list(np.asarray(dx1) + 92))
des3a.append(list(np.asarray(dy1) + 190.5))

#dual 3a 
dual_fun(src3,des3a)
if dd3 == 1:
    plt.scatter(dual[16],dual[17],color='#60efb8',label='dual 3a')

#destination 3b
des3b = []
des3b.append(list(np.asarray(dx1) + 78))
des3b.append(list(np.asarray(dy1) + 240.5))

#dual 3b 
dual_fun(src3,des3b)
if dd3 == 1:
    plt.scatter(dual[18],dual[19],color='#20c1bd',label='dual 3b')

#destination 3c
des3c = []
des3c.append(list(np.asarray(dx1) + 60))
des3c.append(list(np.asarray(dy1) + 258.5))

#dual 3c 
dual_fun(src3,des3c)
if dd3 == 1:
    plt.scatter(dual[20],dual[21],color='#f9e75e',label='dual 3c')

#destination 3d
des3d = []
des3d.append(list(np.asarray(dx1) + 42))
des3d.append(list(np.asarray(dy1) + 274.5))

#dual 3d 
dual_fun(src3,des3d)
if dd3 == 1:
    plt.scatter(dual[22],dual[23],color='#658525',label='dual 3d')

#destination 3e
des3e = []
des3e.append(list(np.asarray(dx1)- 8))
des3e.append(list(np.asarray(dy1)+290))

#source 4
src4 = []
src4.append(list(np.asarray(ox1) + 199))
src4.append(list(np.asarray(oy1) + 198))

#destination 4a
des4a = []
des4a.append(list(np.asarray(dx1) + 292))
des4a.append(list(np.asarray(dy1) + 190.5))

#dual 4a 
dual_fun(src4,des4a)
if dd4 == 1:
    plt.scatter(dual[24],dual[25],color='#ff5f5f',label='dual 4a')

#destination 4b
des4b = []
des4b.append(list(np.asarray(dx1) + 278))
des4b.append(list(np.asarray(dy1) + 240.5))

#dual 4b 
dual_fun(src4,des4b)
if dd4 == 1:
    plt.scatter(dual[26],dual[27],color='#ff6600',label='dual 4b')

#destination 4c
des4c = []
des4c.append(list(np.asarray(dx1) + 260))
des4c.append(list(np.asarray(dy1) + 258.5))

#dual 4c 
dual_fun(src4,des4c)
if dd4 == 1:
    plt.scatter(dual[28],dual[29],color='#00818a',label='dual 4c')

#destination 4d
des4d = []
des4d.append(list(np.asarray(dx1) + 242))
des4d.append(list(np.asarray(dy1) + 274.5))

#dual 4d 
dual_fun(src4,des4d)
if dd4 == 1:
    plt.scatter(dual[30],dual[31],color='#eaafaf',label='dual 4d')

#destination 4e
des4e = []
des4e.append(list(np.asarray(dx1)+ 192))
des4e.append(list(np.asarray(dy1)+290))

#source 5
src5 = []
src5.append(list(np.asarray(ox1) + 499))
src5.append(list(np.asarray(oy1) + 298))

#destination 5a
des5a = []
des5a.append(list(np.asarray(dx1) + 592))
des5a.append(list(np.asarray(dy1) + 290.5))

#dual 5a 
dual_fun(src5,des5a)
if dd5 == 1:
    plt.scatter(dual[32],dual[33],color='#6C7A89',label='dual 5a')

#destination 5b
des5b = []
des5b.append(list(np.asarray(dx1) + 578))
des5b.append(list(np.asarray(dy1) + 340.5))

#dual 5b 
dual_fun(src5,des5b)
if dd5 == 1:
    plt.scatter(dual[34],dual[35],color='#D2D7D3',label='dual 5b')

#destination 5c
des5c = []
des5c.append(list(np.asarray(dx1) + 560))
des5c.append(list(np.asarray(dy1) + 358.5))

#dual 5c 
dual_fun(src5,des5c)
if dd5 == 1:
    plt.scatter(dual[36],dual[37],color='#95A5A6',label='dual 5c')

#destination 5d
des5d = []
des5d.append(list(np.asarray(dx1) + 542))
des5d.append(list(np.asarray(dy1) + 374.5))

#dual 5d 
dual_fun(src5,des5d)
if dd5 == 1:
    plt.scatter(dual[38],dual[39],color='#ABB7B7',label='dual 5d')

#destination 5e
des5e = []
des5e.append(list(np.asarray(dx1)+ 492))
des5e.append(list(np.asarray(dy1)+ 390))

#dual 11 
#dual_fun(src11,des11)
#plt.scatter(dual[20],dual[21],color='#9AECDB',label='dual 11')
plt.legend()
plt.grid()
plt.figure()
plt.show()

plt.scatter(src1[0],src1[1],color='#F89406',label='source 1')
plt.scatter(des1a[0],des1a[1],color='#F03434',label='destination 1a')
plt.scatter(des1b[0],des1b[1],color='#EC644B',label='destination 1b')
plt.scatter(des1c[0],des1c[1],color='#D24D57',label='destination 1c')
plt.scatter(des1d[0],des1d[1],color='#F22613',label='destination 1d')
plt.scatter(des1e[0],des1e[1],color='#E74C3C',label='destination 1e')
plt.scatter(src2[0],src2[1],color='#FABE58',label='source 2')
plt.scatter(des2a[0],des2a[1],color='#013243',label='destination 2a')
plt.scatter(des2b[0],des2b[1],color='#446CB3',label='destination 2b')
plt.scatter(des2c[0],des2c[1],color='#E4F1FE',label='destination 2c')
plt.scatter(des2d[0],des2d[1],color='#4183D7',label='destination 2d')
plt.scatter(des2e[0],des2e[1],color='#59ABE3',label='destination 2e')
plt.scatter(src3[0],src3[1],color='#DB0A5B',label='source 3')
plt.scatter(des3a[0],des3a[1],color='#947CB0',label='destination 3a')
plt.scatter(des3b[0],des3b[1],color='#DCC6E0',label='destination 3b')
plt.scatter(des3c[0],des3c[1],color='#663399',label='destination 3c')
plt.scatter(des3d[0],des3d[1],color='#674172',label='destination 3d')
plt.scatter(des3e[0],des3e[1],color='#913D88',label='destination 3e')
plt.scatter(src4[0],src4[1],color='#663399',label='source 4')
plt.scatter(des4a[0],des4a[1],color='#00E640',label='destination 4a')
plt.scatter(des4b[0],des4b[1],color='#91B496',label='destination 4b')
plt.scatter(des4c[0],des4c[1],color='#4ECDC4',label='destination 4c')
plt.scatter(des4d[0],des4d[1],color='#26A65B',label='destination 4d')
plt.scatter(des4e[0],des4e[1],color='#16A085',label='destination 4e')
plt.scatter(src5[0],src5[1],color='#4ECDC4',label='source 5')
plt.scatter(des5a[0],des5a[1],color='#E87E04',label='destination 5a')
plt.scatter(des5b[0],des5b[1],color='#F4B350',label='destination 5b')
plt.scatter(des5c[0],des5c[1],color='#F2784B',label='destination 5c')
plt.scatter(des5d[0],des5d[1],color='#EB974E',label='destination 5d')
plt.scatter(des5e[0],des5e[1],color='#F9690E',label='destination 5e')
#plt.legend(loc = 'best')
plt.grid()
#plt.figure()
plt.show()