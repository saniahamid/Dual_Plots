# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:43:52 2018

@author: hamid
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 12:36:18 2018

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
src1.append(list(np.asarray(ox1)-1))
src1.append(list(np.asarray(oy1)-2))

#destination 1a
des1a = []
des1a.append(list(np.asarray(dx1)+0))
des1a.append(list(np.asarray(dy1)-9.5))

#dual 1a 
dual_fun(src1,des1a)
plt.scatter(dual[0],dual[1],color='#003545',label='dual 1a')
plt.show()


#destination 1b
des1b = []
des1b.append(list(np.asarray(dx1)- 1.5))
des1b.append(list(np.asarray(dy1)- 4.5))

#dual 1b 
dual_fun(src1,des1b)
plt.scatter(dual[2],dual[3],color='#ed6363',label='dual 1b')
print(dual)
plt.show()

#destination 1c
des1c = []
des1c.append(list(np.asarray(dx1)- 5))
des1c.append(list(np.asarray(dy1)- 2))

#dual 1c 
dual_fun(src1,des1c)
plt.scatter(dual[4],dual[5],color='#90aeff',label='dual 1c')

#destination 1d
des1d = []
des1d.append(list(np.asarray(dx1)- 8))
des1d.append(list(np.asarray(dy1)- 1))

#dual 1d 
dual_fun(src1,des1d)
#plt.scatter(dual[6],dual[7],color='#cefc86',label='dual 1d')

#destination 2a
des2a = []
des2a.append(list(np.asarray(dx1)+ 10))
des2a.append(list(np.asarray(dy1)- 9.5))

#dual 2a 
dual_fun(src1,des2a)
plt.scatter(dual[8],dual[9],color='#60efb8',label='dual 2a')

#destination 2b
des2b = []
des2b.append(list(np.asarray(dx1)+ 7))
des2b.append(list(np.asarray(dy1)- 4.5))

#dual 2b 
dual_fun(src1,des2b)
plt.scatter(dual[10],dual[11],color='#6900ff',label='dual 2b')

#destination 2c
des2c = []
des2c.append(list(np.asarray(dx1) + 3))
des2c.append(list(np.asarray(dy1) + 0))

#dual 2c 
dual_fun(src1,des2c)
plt.scatter(dual[12],dual[13],color='#ffd700',label='dual 2c')

#destination 2d
des2d = []
des2d.append(list(np.asarray(dx1) - 2))
des2d.append(list(np.asarray(dy1) + 5))

#dual 2d 
dual_fun(src1,des2d)
plt.scatter(dual[14],dual[15],color='#c4e3cb',label='dual 2d')

#destination 2e
des2e = []
des2e.append(list(np.asarray(dx1) - 8))
des2e.append(list(np.asarray(dy1)+ 9))

#dual 2d 
dual_fun(src1,des2e)
#plt.scatter(dual[16],dual[17],color='#333366',label='dual 2e')

#destination 3a
des3a = []
des3a.append(list(np.asarray(dx1) + 100))
des3a.append(list(np.asarray(dy1) - 9.5))

#dual 3a 
dual_fun(src1,des3a)
plt.scatter(dual[18],dual[19],color='#fbffa8',label='dual 3a')

#destination 3b
des3b = []
des3b.append(list(np.asarray(dx1) + 92))
des3b.append(list(np.asarray(dy1) + 20.5))

#dual 3b 
dual_fun(src1,des3b)
plt.scatter(dual[20],dual[21],color='#658525',label='dual 3b')

#destination 3c
des3c = []
des3c.append(list(np.asarray(dx1) + 72))
des3c.append(list(np.asarray(dy1) + 40.5))

#dual 3c 
dual_fun(src1,des3c)
plt.scatter(dual[22],dual[23],color='#524c84',label='dual 3c')
            
#destination 3d
des3d = []
des3d.append(list(np.asarray(dx1) + 48))
des3d.append(list(np.asarray(dy1) + 60.5))

#dual 3d 
dual_fun(src1,des3d)
plt.scatter(dual[24],dual[25],color='#20c1bd',label='dual 3d')
            
#destination 3e
des3e = []
des3e.append(list(np.asarray(dx1) + 26))
des3e.append(list(np.asarray(dy1) + 80.5))

#dual 3e 
dual_fun(src1,des3e)
plt.scatter(dual[26],dual[27],color='#404b69',label='dual 3e')
            
#destination 3f
des3f = []
des3f.append(list(np.asarray(dx1) + 6))
des3f.append(list(np.asarray(dy1) + 91.5))

#dual 3f 
dual_fun(src1,des3f)
plt.scatter(dual[28],dual[29],color='#ce2525',label='dual 3f')

#destination 3g
des3g = []
des3g.append(list(np.asarray(dx1) - 8))
des3g.append(list(np.asarray(dy1) + 100))

#dual 3g 
dual_fun(src1,des3g)
#plt.scatter(dual[30],dual[31],color='#00818a',label='dual 3g')

#destination 4a
des4a = []
des4a.append(list(np.asarray(dx1) + 1000))
des4a.append(list(np.asarray(dy1) - 9.5))

#dual 4a 
dual_fun(src1,des4a)
plt.scatter(dual[32],dual[33],color='#f62a66',label='dual 4a')
            
#destination 4m
des4m = []
des4m.append(list(np.asarray(dx1) - 8))
des4m.append(list(np.asarray(dy1) + 1000))

#destination 10
des10 = []
des10.append(list(np.asarray(dx1)+ 0))
des10.append(list(np.asarray(dy1)+ 0))

##dual 11 
#dual_fun(src11,des11)
#plt.scatter(dual[20],dual[21],color='#9AECDB',label='dual 11')
plt.legend()
plt.grid()
plt.figure()
plt.show()

#l = [] 
#list1 = []
#l.append(ox1)
#l.append(oy1)
#l[0] = list(np.asarray(l[0]) + 1)
#print("l 0 is",l[0])
#print("l 1 is",l[1])

plt.scatter(src1[0],src1[1],color='#feca57',label='source 1')
plt.scatter(des1a[0],des1a[1],color='#013243',label='destination 1a')
plt.scatter(des1b[0],des1b[1],color='#19B5FE',label='destination 1b')
plt.scatter(des1c[0],des1c[1],color='#E4F1FE',label='destination 1c')
plt.scatter(des1d[0],des1d[1],color='#4183D7',label='destination 1d')
plt.scatter(des2a[0],des2a[1],color='#F03434',label='destination 2a')
plt.scatter(des2b[0],des2b[1],color='#EC644B',label='destination 2b')
plt.scatter(des2c[0],des2c[1],color='#F22613',label='destination 2c')
plt.scatter(des2d[0],des2d[1],color='#96281B',label='destination 2d')
plt.scatter(des2e[0],des2e[1],color='#D24D57',label='destination 2e')
plt.scatter(des3a[0],des3a[1],color='#00E640',label='destination 3a')
plt.scatter(des3b[0],des3b[1],color='#91B496',label='destination 3b')
plt.scatter(des3c[0],des3c[1],color='#4ECDC4',label='destination 3c')
plt.scatter(des3d[0],des3d[1],color='#87D37C',label='destination 3d')
plt.scatter(des3e[0],des3e[1],color='#26A65B',label='destination 3e')
plt.scatter(des3f[0],des3f[1],color='#1BA39C',label='destination 3f')
plt.scatter(des3g[0],des3g[1],color='#00E640',label='destination 3g')
plt.scatter(des4a[0],des4a[1],color='#FABE58',label='destination 4a')
plt.scatter(des4m[0],des4m[1],color='#E9D460',label='destination 4m')
#plt.scatter(src8[0],src8[1],color='#341f97',label='source 8')
#plt.scatter(des8[0],des8[1],color='#ee5253',label='destination 8')
#plt.scatter(src9[0],src9[1],color='#222f3e',label='source 9')
#plt.scatter(des9[0],des9[1],color='#ee5253',label='destination 9')
#plt.scatter(src10[0],src10[1],color='#FEA47F',label='source 10')
plt.scatter(des10[0],des10[1],color='#82589F',label='destination 10')
#plt.scatter(src11[0],src11[1],color='#9AECDB',label='source 11')
#plt.scatter(des11[0],des11[1],color='#BDC581',label='destination 11')
plt.legend(loc = 'best')
plt.grid()
plt.figure()
plt.show()

 