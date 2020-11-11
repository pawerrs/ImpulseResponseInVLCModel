def get_headers():
    channel_impulse_response_headers = []
    for i in range(122):
        channel_impulse_response_headers.append("power_{}".format(i))

    random_room_parameters_headers = ['room_x1', 'room_x2', 'room_y1', 'room_y2', 'room_z1', 'room_z2', 
    'transmitter_xs', 'transmitter_ys', 'transmitter_zs', 'reflectances']

    return random_room_parameters_headers + channel_impulse_response_headers 