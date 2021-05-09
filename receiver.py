import math
import numpy as np

def receive(P,initial_distance, transmitter_xs,transmitter_ys,transmitter_zs,lambertian_angle_of_ray,random_angle,v,room_x1,room_x2,room_y1,room_y2,room_z1,room_z2,receiver_xyz,receiver_position,field_of_view,sc,number_of_reflection,number_of_reflectances,gof,src,Ax,Tx):

    #unit wectors perpendicular to walls & reflectance
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

    #reflectivity
    # wall, ceiling = 0.8
    # floor = 0.3
    ref=[0.8, 0.8, 0.8, 0.8, 0.3, 0.8]
    
    # default 1
    if(number_of_reflection==1):
        r = abs(math.tan(math.radians(lambertian_angle_of_ray))*math.sqrt(np.dot(n,n)))
        xe = transmitter_xs + math.cos(math.radians(random_angle))*r
        ye = transmitter_ys + math.sin(math.radians(random_angle))*r
        ze = transmitter_zs + math.sqrt(np.dot(n,n))*n[2]
        v1=[xe-transmitter_xs, ye-transmitter_ys, ze-transmitter_zs]
        v=np.asarray(v1)/math.sqrt(np.dot(v1,v1))

    # looking for number_of_reflection point on surface and presumed reflection wall
    v1=100*v
    A = []

    if v1[0]<room_x1:
        A.append(room_x1)
    elif v1[0]>room_x2:
        A.append(room_x2)
    else:
        A.append(0.5*(room_x1+room_x2))

    if v1[1]<room_y1:
        A.append(room_y1)
    elif v1[1]>room_y2:
        A.append(room_y2)
    else:
        A.append(0.5*(room_y1+room_y2))

    if v1[2]<room_z1:
       A.append(room_z1)
    elif v1[2]>room_z2:
       A.append(room_z2)
    else:
       A.append(0.5*(room_z1+room_z2))

    dv=0.1*v
    v1=[transmitter_xs, transmitter_ys, transmitter_zs]

    end_flag=0
    while end_flag==0:
        v1=v1+dv
        if v1[0]<=room_x1:
            sc=1
            end_flag=1
        elif v1[0]>=room_x2:
            sc=3
            end_flag=1
        elif v1[1]<=room_y1:
            sc=2
            end_flag=1
        elif v1[1]>=room_y2:
            sc=4
            end_flag=1
        elif v1[2]<=room_z1:
            sc=5
            end_flag=1
        elif v1[2]>=room_z2:
            sc=6
            end_flag=1

    # vector operation
    S=[transmitter_xs, transmitter_ys, transmitter_zs]
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

    reflection_point = [OR[0], OR[1], OR[2]]

    # shift of reflection point to wall

    #  distance
    distance_from_start_to_hit_point=math.sqrt(math.pow(reflection_point[0]-transmitter_xs,2)+math.pow(reflection_point[1]-transmitter_ys,2)+math.pow(reflection_point[2]-transmitter_zs,2)) # distance between number_of_reflection start poin and number_of_reflection hit point
    
    #distance traveled by number_of_reflection ray
    distance_traveled_by_ray=initial_distance+distance_from_start_to_hit_point 

    # distance to receiver
    distance_to_receiver=math.sqrt(math.pow(transmitter_xs-receiver_xyz[0],2)+math.pow(transmitter_ys-receiver_xyz[1],2)+math.pow(transmitter_zs-receiver_xyz[2],2))

    # field_of_view
    vi=[transmitter_xs-receiver_xyz[0], transmitter_ys-receiver_xyz[1], transmitter_zs-receiver_xyz[2]]
    ai = math.degrees(np.arccos(vi[2]/math.sqrt(np.dot(vi,vi))))

    #time when ray arrives road divided by speed of light
    Tx[number_of_reflection-1]=(initial_distance+distance_to_receiver)/(3*math.pow(10,8))

    if reflection_point[0]>=receiver_position[0] and reflection_point[0]<=receiver_position[1] and reflection_point[1]>=receiver_position[2] and reflection_point[1]<=receiver_position[3] and reflection_point[2]==receiver_position[4]:
        stop_execution=1
    else:
        stop_execution=0

    if abs(ai)<field_of_view:
        if number_of_reflection==1:
            Ax[number_of_reflection-1]=(P/(math.pi*math.pow(initial_distance+distance_to_receiver,2)))*math.cos(math.radians(ai))
        else:
            Ax[number_of_reflection-1]=(P/(math.pow(initial_distance+distance_to_receiver,2)))*math.cos(math.radians(ai))
    else:
        Ax[number_of_reflection-1]=0

    if stop_execution==0:
        P=P*ref[sc-1]

    # now point of light source
    transmitter_xs=reflection_point[0]
    transmitter_ys=reflection_point[1]
    transmitter_zs=reflection_point[2]

    # new unit reflection vector, snells law
    v=v-(2*np.dot(v,ni)*np.asarray(ni))

    if np.isfinite(P) and distance_traveled_by_ray != 0:
        Px=P/(math.pow(distance_traveled_by_ray,2))
    else:
        Px=0
        P=0

    tx=(initial_distance+distance_from_start_to_hit_point)/(3*math.pow(10,8))

    #ray did not arrive to receiver
    if number_of_reflection==number_of_reflectances and stop_execution==0:
        Px=0

    number_of_reflection=number_of_reflection+1

    if number_of_reflection<=number_of_reflectances and stop_execution==0:
        Px,distance_traveled_by_ray,tx,Ax,Tx=receive(P,distance_traveled_by_ray,transmitter_xs,transmitter_ys,transmitter_zs,lambertian_angle_of_ray,random_angle,v,room_x1,room_x2,room_y1,room_y2,room_z1,room_z2,receiver_xyz,receiver_position,field_of_view,sc,number_of_reflection,number_of_reflectances,gof,src,Ax,Tx)

    return Px,distance_traveled_by_ray,tx,Ax,Tx






