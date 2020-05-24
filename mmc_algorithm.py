import math
import lambertian
import numpy as np
import receiver
import sort_map_mb
import matplotlib.pyplot as plt

def solve(parameters):

    room_x1 = parameters[0]
    room_x2 = parameters[1]
    room_y1 = parameters[2]
    room_y2 = parameters[3]
    room_z1 = parameters[4]
    room_z2 = parameters[5]
    transmitter_xs = parameters[6]
    transmitter_ys = parameters[7]
    transmitter_zs = parameters[8]
    number_of_reflectances = parameters[9]

    gof = 0
    a = 1

    # number of generated rays
    N = math.pow(10,4)

    # position of receiver
    rx = 0.01
    Ar = math.pow(rx,2)
    Rt = [-1, -1, 0]

    receiver_x1 = Rt[0] - rx
    receiver_x2 = Rt[0] + rx
    receiver_y1 = Rt[1] - rx
    receiver_y2 = Rt[1] + rx
    receiver_z1 = Rt[2]
    receiver_z2 = Rt[2] + rx

    Rtx=[receiver_x1, receiver_x2, receiver_y1, receiver_y2, receiver_z1, receiver_z2]

    # LED SemiAngle
    SemiAngle = 60

    # Field Of View of detector
    FOV = 85

    v = [0, 0, 0]

    m = -math.log(2)/(math.log(math.cos(math.radians(SemiAngle))))
    AS = lambertian.calculate(N,1)
    FI = 360 * np.random.uniform(0,1,int(N))
    P = 1/N

    h = np.zeros([int(N),3],dtype = np.float)
    Ax =  np.zeros([number_of_reflectances,1],dtype = np.float)
    Tx =  np.zeros([number_of_reflectances,1],dtype = np.float)
    Ax1 = np.zeros([number_of_reflectances,int(N)],dtype = np.float)
    Tx1 = np.zeros([number_of_reflectances,int(N)],dtype = np.float)

    for i in range(0, int(N)):
        Pxprim,Dxprim,txprim,Axprim,Txprim = receiver.receive(P,0,m,transmitter_xs,transmitter_ys,transmitter_zs,AS[i],FI[i],v,room_x1,room_x2,room_y1,room_y2,room_z1,room_z2,Rt,Rtx,FOV,6,a,number_of_reflectances,gof,0,Ax,Tx)
        h[i,0] = Pxprim
        h[i,1] = Dxprim
        h[i,2] = txprim
        for x in range(0, number_of_reflectances):
            Ax1[x,i] = Axprim[x]
            Tx1[x,i] = Txprim[x]

    Ax1=np.asarray(Ax1)*Ar
    time,r2=sort_map_mb.sort(Ax1,Tx1,0.5,60)

    power = np.concatenate([math.pow(10,6)*x for x in r2]).ravel().tolist()


    return power
