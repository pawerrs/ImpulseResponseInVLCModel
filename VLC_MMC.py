import math
import lambertian
import numpy as np
import logging
import receiver
import sort_map_mb
import matplotlib.pyplot as plt

sk = 2
c = 3*math.pow(10,8)
gof = 0

a = 1

# number of reflectances
b = 31

# number of generated rays
N = math.pow(10,4)

# room coordinates
x1 =-2.5
x2 =2.5

y1 =-2.5
y2 =2.5

z1 = 0
z2 =3 

# position of transmitter
xs = 0.0
ys = 0.0
zs = 3

# position of receiver
rx = 0.01
Ar = math.pow(rx,2)
Rt = [-1, -1, 0]

x1r = Rt[0] - rx
x2r = Rt[0] + rx
y1r = Rt[1] - rx
y2r = Rt[1] + rx
z1r = Rt[2]
z2r = Rt[2] + rx

Rtx=[x1r, x2r, y1r, y2r, z1r, z2r]

# LED SemiAngle
SemiAngle = 60

# FOV of detector
FOV = 85

v = [0, 0, 0]

m = -math.log(2)/(math.log(math.cos(math.radians(SemiAngle))))
AS = lambertian.calculate(N,1)
FI = 360 * np.random.uniform(0,1,int(N))
P = 1/N

h = np.zeros([int(N),3],dtype = np.float)
Ax =  np.zeros([b,1],dtype = np.float)
Tx =  np.zeros([b,1],dtype = np.float)
Ax1 = np.zeros([b,int(N)],dtype = np.float)
Tx1 = np.zeros([b,int(N)],dtype = np.float)

for i in range(0, int(N)):
    Pxprim,Dxprim,txprim,Axprim,Txprim = receiver.receive(P,0,m,xs,ys,zs,AS[i],FI[i],v,x1,x2,y1,y2,z1,z2,Rt,Rtx,FOV,6,a,b,gof,0,Ax,Tx)
    h[i,0] = Pxprim
    h[i,1] = Dxprim
    h[i,2] = txprim
    for x in range(0, b):
        Ax1[x,i] = Axprim[x]
        Tx1[x,i] = Txprim[x]

Ax1=np.asarray(Ax1)*Ar
r1,r2=sort_map_mb.sort(Ax1,Tx1,0.5,60)


l = [math.pow(10,6)*x for x in r2]
plt.plot(r1, l)
plt.xlabel('Impulse response')
plt.ylabel('Position ')
plt.show()
