import math
import lambertian
import numpy as np
import receiver
import sort_map_mb
import matplotlib.pyplot as plt

def compute(parameters, draw_chart):

    time_length = 60
    time_between_samples = 0.5

    #room parameters
    room_x1 = parameters[0]
    room_x2 = parameters[1]
    room_y1 = parameters[2]
    room_y2 = parameters[3]
    room_z1 = parameters[4]
    room_z2 = parameters[5]

    #transmitter
    transmitter_xs = parameters[6]
    transmitter_ys = parameters[7]
    transmitter_zs = parameters[8]

    #reflectances
    number_of_reflectances = parameters[12]

    gof = 0
    a = 1
    sc = 6

    # number of generated tracing rays
    N = 10000

    rx = 0.01
    Ar = math.pow(rx,2)
    receiver_xyz = [parameters[9], parameters[10], parameters[11]]

    #receiver position
    receiver_position=[receiver_xyz[0] - rx, receiver_xyz[0] + rx, receiver_xyz[1] - rx, receiver_xyz[1] + rx, receiver_xyz[2], receiver_xyz[2] + rx]

    # Field Of View of detector
    field_of_view = 85

    v = [0, 0, 0]

    initial_distance = 0

    #generalized Lambertian radiant intensity model
    lambertian_angles_of_rays = lambertian.calculate(N,1)

    # N-samples uniformly distributed between (1, 360)
    random_angle = 360 * np.random.uniform(0,1,int(N))

    #reciprocal of the number of beams, power ber beam
    P = 1/N

    #generating arrays filled witz zeros, second parameter is number of array dimensions
    Ax =  np.zeros([number_of_reflectances,1],dtype = np.float)
    Tx =  np.zeros([number_of_reflectances,1],dtype = np.float)
    Ax1 = np.zeros([number_of_reflectances,int(N)],dtype = np.float)
    Tx1 = np.zeros([number_of_reflectances,int(N)],dtype = np.float)

    #loop through every ray
    for i in range(0, int(N)):
        Pxprim,distance_traveled_by_ray,txprim,Axprim,Txprim = receiver.receive(P,initial_distance,transmitter_xs,transmitter_ys,transmitter_zs,lambertian_angles_of_rays[i],random_angle[i],v,room_x1,room_x2,room_y1,room_y2,room_z1,room_z2,receiver_xyz,receiver_position,field_of_view,sc,a,number_of_reflectances,gof,0,Ax,Tx)
        for x in range(0, number_of_reflectances):
            Ax1[x,i] = Axprim[x]
            Tx1[x,i] = Txprim[x]

    Ax1=np.asarray(Ax1)*Ar
    time,r2=sort_map_mb.sort(Ax1,Tx1,time_between_samples,time_length)

    r2[-1] = r2[-2]
    power = np.concatenate([math.pow(10,6)*x for x in r2]).ravel().tolist()

    if draw_chart:
        l = [math.pow(10,6)*x for x in r2]
        fig, ax = plt.subplots()
        plt.plot(time, l)
        plt.xlabel('Czas [ns]')
        plt.ylabel('Odpowiedź impulsowa [x10^-6 1/s]')

        textstr = '\n'.join((
            r'$Pomieszczenie= %.1f x %.1f x %.1f$' % (room_x2 - room_x1, room_y2 - room_y1, room_z2 - room_z1,  ),
            r'$Nadajnik=[%.1f, %.1f, %.1f]$' % (transmitter_xs, transmitter_ys, transmitter_zs,  ),
            r'$Odbiornik=[%.1f, %.1f, %.1f]$' % (receiver_xyz[0], receiver_xyz[1], receiver_xyz[2], )))

        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        ax.text(0.55, 0.9, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
        plt.show()

    return power
