import math
import numpy as np

def receive(P,D,m,xs,ys,zs,AS,fi,v,x1,x2,y1,y2,z1,z2,Rt,Rtx,FOV,sc,a,b,gof,src,Ax,Tx):

    if(sc == 1):
        n = [1,0,0]
    elif(sc == 2):
        n = [0,1,0]
    elif(sc == 3):
        n = [-1,0,0]
    elif(sc == 4):
        n = [0,-1,0]
    elif(sc == 5):
        n = [0,0,1]
    elif sc==6:
        n = [0,0,-1]

    ref=[0.8, 0.8, 0.8, 0.8, 0.3, 0.8]
    
    if(a==1):
        r = abs(math.tan(math.radians(AS))*math.sqrt(np.dot(n,n)))
        xe = xs + math.cos(math.radians(fi))*r
        ye = ys + math.sin(math.radians(fi))*r
        ze = zs + math.sqrt(np.dot(n,n))*n[2]
        v1=[xe-xs, ye-ys, ze-zs]
        v=np.asarray(v1)/math.sqrt(np.dot(v1,v1))

    # we looking for a point on surface and presumed reflection wall
    v1=100*v
    A = []

    if v1[0]<x1:
        A.append(x1)
    elif v1[0]>x2:
        A.append(x2)
    else:
        A.append(0.5*(x1+x2))

    if v1[1]<y1:
        A.append(y1)
    elif v1[1]>y2:
        A.append(y2)
    else:
        A.append(0.5*(y1+y2))

    if v1[2]<z1:
       A.append(z1)
    elif v1[2]>z2:
       A.append(z2)
    else:
       A.append(0.5*(z1+z2))


    dv=0.1*v
    v1=[xs, ys, zs]

    end_flag=0
    while end_flag==0:
        v1=v1+dv
        if v1[0]<=x1:
            sc=1
            end_flag=1
        elif v1[0]>=x2:
            sc=3
            end_flag=1
        elif v1[1]<=y1:
            sc=2
            end_flag=1
        elif v1[1]>=y2:
            sc=4
            end_flag=1
        elif v1[2]<=z1:
            sc=5
            end_flag=1
        elif v1[2]>=z2:
            sc=6
            end_flag=1

    # vector operation
    S=[xs, ys, zs]
    O=[0,0,0]
    SA=np.asarray(A)-np.asarray(S)
    OS=np.asarray(S)-np.asarray(O)

    if sc==1:
        ni=[1, 0, 0]
    elif sc==2:
        ni=[0, 1, 0]
    elif sc==3:
        ni=[-1, 0, 0]
    elif sc==4:
        ni=[0, -1, 0]
    elif sc==5:
        ni=[0, 0, 1]
    elif sc==6:
        ni=[0, 0, -1]


    OR=OS+(np.dot(ni,SA)/np.dot(ni,v))*v

    R = [OR[0], OR[1], OR[2]]

    # shift of reflection point to wall

    #  distance
    D1=math.sqrt(math.pow(R[0]-xs,2)+math.pow(R[1]-ys,2)+math.pow(R[2]-zs,2)) # distance between a start poin and a hit point
    Dx=D+D1 #distance traveled by a ray
    DR=math.sqrt(math.pow(xs-Rt[0],2)+math.pow(ys-Rt[1],2)+math.pow(zs-Rt[2],2)) # distance to receiver

    # FOV
    vi=[xs-Rt[0], ys-Rt[1], zs-Rt[2]]
    ai = math.degrees(np.arccos(vi[2]/math.sqrt(np.dot(vi,vi))))
    Tx[a-1]=(D+DR)/(3*math.pow(10,8))

    # print(str(a))
    if R[0]>=Rtx[0] and R[0]<=Rtx[1] and R[1]>=Rtx[2] and R[1]<=Rtx[3] and R[2]==Rtx[4]:
        print('A ray obtained receiver: ' + str(a))
        stop_flag=1
    else:
        stop_flag=0


    if abs(ai)<FOV:
        if a==1:
            Ax[a-1]=(P/(math.pow(math.pi,2)*math.pow(D+DR,2)))*math.cos(math.radians(ai))
        else:
            Ax[a-1]=(P/(math.pow(D+DR,2)))*math.cos(math.radians(ai))
    else:
        Ax[a-1]=0


    if stop_flag==0:
        P=P*ref[sc-1]


    # now point of light source
    xs=R[0]
    ys=R[1]
    zs=R[2]

    # new unit reflection vector

    v=v-(2*np.dot(v,ni)*np.asarray(ni))

    if np.isfinite(P):
        Px=P/(math.pow(Dx,2))
    else:
        Px=0
        P=0

    tx=(D+D1)/(3*math.pow(10,8))

    if a==b and stop_flag==0:
        Px=0

    a=a+1

    # print('Px: ' + str(Px)) 
    # print(' Dx:' + str(Dx))
    # print(' tx: ' + str(tx))
    # print(' Ax: '  + str(Ax))
    # print(' Tx: ' + str(Tx))
    



    if a<=b and stop_flag==0:
        Px,Dx,tx,Ax,Tx=receive(P,Dx,m,xs,ys,zs,AS,fi,v,x1,x2,y1,y2,z1,z2,Rt,Rtx,FOV,sc,a,b,gof,src,Ax,Tx)

    return Px,Dx,tx,Ax,Tx






