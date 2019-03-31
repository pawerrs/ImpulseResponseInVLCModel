from operator import itemgetter
import numpy as np
import math

def sort(Ax1,Tx1,ds,t_max):

    s = Ax1.shape
    Ax_map = zeros(s[0]*s[1],1)
    Tx_map = zeros(s([0]*s[1],1)

    for i in range(0,s[1]):
        Ax_map(1+s[0]*(i-1):s[0]*i,1)=Ax1[:,i]
        Tx_map(1+s[0]*(i-1):s[0]*i,1)=Tx1[:,i]

    al,bl=zip(*sorted(enumerate(Tx_map), key=itemgetter(1)))
    a = list(al)
    b = list(bl)
    c=np.zeros([len(Ax_map),1)], dtype = int)
    for i in range (0,len(b)):
        c[i]=Ax_map[b[i],1]  # moc

    h_new=[a,c]

    t = []
    x=0;
    while x <= t_max:
        t.append(x)
        x = x + ds
    
    tp=np.zeros(len(t),1)

    for k in range(0, len(a)):
        ii = np.se
        ii = next(obj for obj in objs if t => a[k] * math.pow(10,9))
        ii=find(t>=a(k)*10^9,1,'first')
        if np.isfinite(c[k]) and c[k]>0:
            tp[ii]=tp[ii]+c[k]


    return np.asarray(t).transpose(), tp
