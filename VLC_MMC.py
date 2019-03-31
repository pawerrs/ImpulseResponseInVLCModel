import math
import lambertian
import numpy as np
import logging
import receiver
#import sort_map_mb

sk = 2
c = 3*math.pow(10,8)
gof = 0

a = 1
b = 31

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

h = np.zeros([int(N),3],dtype = int)
Ax =  np.zeros([b,1],dtype = int)
Tx =  np.zeros([b,1],dtype = int)
Ax1 = np.zeros([b,int(N)],dtype = int)
Tx1 = np.zeros([b,int(N)],dtype = int)

for i in range(0, int(N-1)):
    if (i%(int(N)/100))==0:
        print("wykonano: ")
    h[i,0],h[i,1],h[i,2],Ax1[:,i],Tx1[:,i] = receiver.receive(P,0,m,xs,ys,zs,AS[i],FI[i],v,x1,x2,y1,y2,z1,z2,Rt,Rtx,FOV,6,a,b,gof,0,Ax,Tx)


Ax1=np.asarray(Ax1)*Ar;
r=sort_map_mb.sort(Ax1,Tx1,0.5,60);

# figure(3)
# plot(r(:,1),r(:,2)*10^6)


# clc
# display('channel statistical parameters')
# u=sum((r(:,2)).^2.*r(:,1))/sum(r(:,2).^2)
# Drms=sqrt(sum((r(:,1)-u).^2.*r(:,2).^2)/sum(r(:,2).^2))
# Ho=sum((r(:,2)).^2.*r(:,1))
# g=find(r(:,2)>0,1,'first');
# t0=r(g,1)