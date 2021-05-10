import random

def generate_random_input_values(room_max_size):
    room_x1 = round(random.uniform(-room_max_size/2, -0.5), 2)
    room_x2 = round(random.uniform(0.5, room_max_size/2), 2)
    room_y1 = round(random.uniform(-room_max_size/2, -0.5), 2)
    room_y2 = round(random.uniform(0.5, 3), 2)
    room_z1 = 0
    room_z2 = 3
    transmitter_xs = round(random.uniform(room_x1, room_x2), 2)
    transmitter_ys = round(random.uniform(room_y1, room_y2), 2)
    transmitter_zs = 3
    receiver_x = round(random.uniform(room_x1, room_x2), 2)
    receiver_y = round(random.uniform(room_y1, room_y2), 2)
    receiver_z = 0
    number_of_reflectances = 20

    # room_x1 = -2
    # room_x2 = 2
    # room_y1 = -2
    # room_y2 = 2
    # room_z1 = 0
    # room_z2 = 3
    # transmitter_xs = -0
    # transmitter_ys = -0
    # transmitter_zs = 3
    # receiver_x = -1
    # receiver_y = -1
    # receiver_z = 0
    # number_of_reflectances = 100

    return [room_x1, room_x2, room_y1, room_y2, room_z1, room_z2, transmitter_xs, transmitter_ys, transmitter_zs, receiver_x, receiver_y, receiver_z, number_of_reflectances]