from matplotlib import pyplot as plt
import numpy as np

ox1=[1,1,1.5,2,3] 
oy1=[2,3,2.3,1.5,2]
dx1=[8,8.5,9,7.9,8]
dy1=[9,10,9.5,10,9.75]
dual = []

def dual_fun(src , des ):
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
src1.append(list(np.asarray(ox1)*0.75))
src1.append(list(np.asarray(oy1)))

#destination 1
des1 = []
des1.append(list(np.asarray(dx1)))
des1.append(list(np.asarray(dy1)))

#dual 1 
dual_fun(src1,des1)
plt.scatter(dual[0],dual[1],color='#feca57',label='dual 1')
#plt.show()

#source 2
src2 = []
src2.append(list(np.asarray(ox1)*0.75 + 0.5))
src2.append(list(np.asarray(oy1)+ 1))

#destination 2
des2 = []
des2.append(list(np.asarray(dx1)+ 10))
des2.append(list(np.asarray(dy1)+ 1))

#dual 2 
dual_fun(src2,des2)
plt.scatter(dual[2],dual[3],color='#54a0ff',label='dual 2')
#print(dual)
#plt.show()

#source 3
src3 = []
src3.append(list(np.asarray(ox1) + 10))
src3.append(list(np.asarray(oy1) + 2))

#destination 3
des3 = []
des3.append(list(np.asarray(dx1)+ 3))
des3.append(list(np.asarray(dy1)+ 1))

#dual 3 
dual_fun(src3,des3)
#plt.scatter(dual[4],dual[5],color='#ff9ff3',label='dual 3')


#source 4
src4 = []
src4.append(list(np.asarray(ox1) + 30))
src4.append(list(np.asarray(oy1) + 4))

#destination 4
des4 = []
des4.append(list(np.asarray(dx1)+ 15))
des4.append(list(np.asarray(dy1)+ 5))

#dual 4 
dual_fun(src4,des4)
plt.scatter(dual[6],dual[7],color='#00d2d3',label='dual 4')


#source 5
src5 = []
src5.append(list(np.asarray(ox1) + 30))
src5.append(list(np.asarray(oy1) + 3))

#destination 5
des5 = []
des5.append(list(np.asarray(dx1)+ 35))
des5.append(list(np.asarray(dy1)+ 5))

#dual 5 
dual_fun(src5,des5)
plt.scatter(dual[8],dual[9],color='#ff6b6b',label='dual 5')

#source 6
src6 = []
src6.append(list(np.asarray(ox1) + 60))
src6.append(list(np.asarray(oy1) + 25))

#destination 6
des6 = []
des6.append(list(np.asarray(dx1)+ 40))
des6.append(list(np.asarray(dy1)+ 10))

#dual 6 
dual_fun(src6,des6)
plt.scatter(dual[10],dual[11],color='#5f27cd',label='dual 6')

#source 7
src7 = []
src7.append(list(np.asarray(ox1) + 60))
src7.append(list(np.asarray(oy1) + 26.5))

#destination 7
des7 = []
des7.append(list(np.asarray(dx1)+ 65))
des7.append(list(np.asarray(dy1)+ 10))

#dual 7 
dual_fun(src7,des7)
plt.scatter(dual[12],dual[13],color='#ff9f43',label='dual 7')

#source 8
src8 = []
src8.append(list(np.asarray(ox1) + 7))
src8.append(list(np.asarray(oy1) + 20))

#destination 8
des8 = []
des8.append(list(np.asarray(dx1)+ 20))
des8.append(list(np.asarray(dy1)+ 13))

#dual 8 
dual_fun(src8,des8)
plt.scatter(dual[14],dual[15],color='#341f97',label='dual 8')

#source 9
src9 = []
src9.append(list(np.asarray(ox1) + 60))
src9.append(list(np.asarray(oy1) + 10))

#destination 9
des9 = []
des9.append(list(np.asarray(dx1) -5))
des9.append(list(np.asarray(dy1)+ 50))

#dual 9 
dual_fun(src9,des9)
#plt.scatter(dual[16],dual[17],color='#222f3e',label='dual 9')

#source 10
src10 = []
src10.append(list(np.asarray(ox1) + 40))
src10.append(list(np.asarray(oy1) + 40))

#destination 10
des10 = []
des10.append(list(np.asarray(dx1)+ 23))
des10.append(list(np.asarray(dy1)+ 22))

#dual 10 
dual_fun(src10,des10)
plt.scatter(dual[18],dual[19],color='#FEA47F',label='dual 10')

#source 11
src11 = []
src11.append(list(np.asarray(ox1) + 40))
src11.append(list(np.asarray(oy1) + 41))

#destination 11
des11 = []
des11.append(list(np.asarray(dx1)+ 45))
des11.append(list(np.asarray(dy1)+ 42))

#dual 11 
dual_fun(src11,des11)
plt.scatter(dual[20],dual[21],color='#9AECDB',label='dual 11')
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
plt.scatter(des1[0],des1[1],color='#54a0ff',label='destination 1')
plt.scatter(src2[0],src2[1],color='#ff9ff3',label='source 2')
plt.scatter(des2[0],des2[1],color='#00d2d3',label='destination 2')
plt.scatter(src3[0],src3[1],color='#ff6b6b',label='source 3')
plt.scatter(des3[0],des3[1],color='#5f27cd',label='destination 3')
plt.scatter(src4[0],src4[1],color='#48dbfb',label='source 4')
plt.scatter(des4[0],des4[1],color='#c8d6e5',label='destination 4')
plt.scatter(src5[0],src5[1],color='#1dd1a1',label='source 5')
plt.scatter(des5[0],des5[1],color='#576574',label='destination 5')
plt.scatter(src6[0],src6[1],color='#01a3a4',label='source 6')
plt.scatter(des6[0],des6[1],color='#f368e0',label='destination 6')
plt.scatter(src7[0],src7[1],color='#2e86de',label='source 7')
plt.scatter(des7[0],des7[1],color='#ff9f43',label='destination 7')
plt.scatter(src8[0],src8[1],color='#341f97',label='source 8')
plt.scatter(des8[0],des8[1],color='#ee5253',label='destination 8')
plt.scatter(src9[0],src9[1],color='#222f3e',label='source 9')
plt.scatter(des9[0],des9[1],color='#ee5253',label='destination 9')
plt.scatter(src10[0],src10[1],color='#FEA47F',label='source 10')
plt.scatter(des10[0],des10[1],color='#82589F',label='destination 10')
plt.scatter(src11[0],src11[1],color='#9AECDB',label='source 11')
plt.scatter(des11[0],des11[1],color='#BDC581',label='destination 11')
plt.legend(loc = 'best')
plt.grid()
plt.figure()
plt.show()
