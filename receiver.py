# import math
# import numpy as np

# def receive (P,D,m,xs,ys,zs,as,fi,v,x1,x2,y1,y2,z1,z2,Rt,Rtx,FOV,sc,a,b,gof,src,Ax,Tx):

#     if(sc == 1):
#         n = [1,0,0]
#     elif(sc == 2):
#         n = [0,1,0]
#     elif(sc == 3):
#         n = [-1,0,0]
#     elif(sc == 4):
#         n = [0,-1,0]
#     elif(sc == 5):
#         n = [0,0,1]
#     elif sc==6
#         n = [0,0,-1];


#     ref=[0.8, 0.8, 0.8, 0.8, 0.3, 0.8];

#     if(a==1):
#         r = abs(math.atan(math.radians(degrees))*math.sqrt(np.dot(n,n)))
#         xe = xs + math.cos(math.radians(fi))*r
#         ye = ys + math.sin(math.radians(fi))*r
#         ze = zs + math.sqrt(np.dot(n,n))*math.pow(n,3)
#         v1=[xe-xs, ye-ys, ze-zs]
#         v=v1/math.sqrt(np.dot(v1,v1))


#     if(gof == 1)
#         #figure (1)
#         # hold on
#         # creation unit vector
#         # plot3([xs v(1)+xs],[ys v(2)+ys],[zs v(3)+zs],'g')
        

#     # we looking for a point on surface and presumed reflection wall
#     v1=100*v;

#     if v1[1]<x1:
#         A[1]=x1
#     elif v1[1]>x2:
#         A[1]=x2
#     else:
#         A[1]=0.5*(x1+x2)


#     if v1[2]<y1:
#         A[2]=y1
#     elif v1[2]>y2:
#          A[2]=y2
#     else:
#         A[2]=0.5*(y1+y2)


#     if v1[3]<z1:
#        A(3)=z1
#     elseif v1[3]>z2:
#        A[3]=z2
#     else
#        A[3]=0.5*(z1+z2)
#     end

#     dv=0.1*v
#     v1=[xs, ys, zs]

#     end_flag=0
#     while end_flag==0:
#         v1=v1+dv
#         if v1[1]<=x1:
#             sc=1
#             end_flag=1
#         elif v1[1]>=x2:
#             sc=3
#             end_flag=1
#         elif v1[2]<=y1:
#             sc=2
#             end_flag=1
#         elif v1[2]>=y2:
#             sc=4
#             end_flag=1
#         elif v1[3]<=z1:
#             sc=5
#             end_flag=1
#         elif v1[3]>=z2:
#             sc=6
#             end_flag=1

#     # vector operation
#     S=[xs, ys, zs]
#     O=[0,0,0]
#     SA=A-S
#     OS=S-O

#     if sc==1:
#         ni=[1 0 0]
#     elif sc==2:
#         ni=[0, 1, 0]
#     elif sc==3:
#         ni=[-1, 0, 0]
#     elif sc==4:
#         ni=[0, -1, 0]
#     elif sc==5:
#         ni=[0, 0, 1]
#     elif sc==6:
#         ni=[0, 0, -1]


#     OR=OS+(np.dot(ni,SA)/np.dot(ni,v))*v

#     #  figure(1)
#     #  hold on
#     #  plot3([S(1) OR(1)],[S(2) OR(2)],[S(3) OR(3)],'r-')

#     R[1]=OR[1]
#     R[2]=OR[2]
#     R[3]=OR[3]

#     # shift of reflection point to wall

#     #  distance
#     D1=math.sqrt(math.pow(R[1]-xs,2)+math.pow(R[2]-ys,2)+math.pow(R[3]-zs,2)) # distance between a start poin and a hit point
#     Dx=D+D1 #distance traveled by a ray
#     DR=math.sqrt(math.pow(xs-Rt[1],2)+math.pow(ys-Rt[2],2)+math.pow(zs-Rt[3],2)) # distance to receiver

#     # FOV
#     vi=[xs-Rt[1], ys-Rt[2], zs-Rt[3]
#     ai = math.acos(math.radians(vi(3)/math.sqrt(np.dot(vi,vi))))
#     Tx[a]=(D+DR)/(3*math.pow(10,8))


#     if R[1]>=Rtx[1] && R[1]<=Rtx[2] && R[2]>=Rtx[3] && R[2]<=Rtx[4] && R[3]==Rtx[5]:
#         display(strcat('A ray obtained receiver: ',' ',num2str(a)))
#         print('A ray obtained receiver: ' + str(a))
#         stop_flag=1
#     else:
#         stop_flag=0
#     end

#     if abs[ai]<FOV: 
#         if a==1:
#             Ax[a]=(P/(math.pow(pi,2)*math.pow((D+DR),2))*math.cos(math.radians(ai))
#         else:
#             Ax[a]=(P/(math.pow((D+DR),2))*math.cos(math.radians(ai))
#     else:
#         Ax[a]=0;


#     if stop_flag==0:
#         P=P*ref[sc]


#     # now point of light source
#     xs=R[1]
#     ys=R[2]
#     zs=R[3]

#     # new unit reflection vector

#     v=v-2*np.dot(v,ni)*ni;

#     if gof==1:
#         # figure(1)
#         # hold on
#         # plot3([S(1) R(1)],[S(2) R(2)],[S(3) R(3)],'m')


#     if np.isfinite(P):
#         Px=P/(math.pow(Dx,2)
#     else:
#         Px=0
#         P=0


#     tx=(D+D1)/(3*math.pow(10,8)

#     if a==b && stop_flag==0:
#         Px=0

#     a=a+1

#     if a<=b && stop_flag==0
#         # P=P*((m+1)/(2*pi))*cosd(as)^m
#         [Px,Dx,tx,Ax,Tx]=receiver.receive(P,Dx,m,xs,ys,zs,as,fi,v,x1,x2,y1,y2,z1,z2,Rt,Rtx,FOV,sc,a,b,gof,src,Ax,Tx);
#     else:
#         return [Px,Dx,tx,Ax,Tx]






