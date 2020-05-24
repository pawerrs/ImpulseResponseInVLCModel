from operator import itemgetter
import numpy as np
import math

def sort(Ax1,Tx1,ds,t_max):

    s = Ax1.shape
    Ax_map = np.zeros([s[0]*s[1],1],dtype = np.float)
    Tx_map = np.zeros([s[0]*s[1],1],dtype = np.float)

    for i in range(1,s[1]+1):
        Ax_map[s[0]*(i-1):(s[0]*i), 0] = Ax1[:,i-1]
        Tx_map[s[0]*(i-1):(s[0]*i), 0] = Tx1[:,i-1]

    a = np.sort(Tx_map,axis=None)
    b = np.argsort(Tx_map,axis=None)
    c=np.zeros([len(Ax_map),1],dtype = np.float)
    for i in range (0,len(b)):
        c[i]=Ax_map[b[i],0]  # moc

    t = []
    x=0
    while x <= t_max:
        t.append(x)
        x = x + ds
    
    tp=np.zeros([len(t),1], dtype = np.float)

    for k in range(0, len(a)):
        ii = [i for i in range(len(t)) if t[i] >= a[k]*math.pow(10,9)]
        if ii: 
            iix = ii[0]
        if np.isfinite(c[k]) and c[k]>0:
            tp[iix]=tp[iix]+c[k]

    return np.asarray(t).transpose(), tp
