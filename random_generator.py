import random

def generate_random_input_values(room_max_size):
    room_x1 = round(random.uniform(-room_max_size, 0), 2)
    room_x2 = round(random.uniform(0, room_max_size), 2)
    room_y1 = round(random.uniform(-room_max_size, 0), 2)
    room_y2 = round(random.uniform(0, room_max_size), 2)
    room_z1 = 0
    room_z2 = round(random.uniform(0, room_max_size), 2)
    transmitter_xs = 0
    transmitter_ys = 0
    transmitter_zs = round(random.uniform(room_z1, room_z2), 2)
    number_of_reflectances = random.randint(20,50)

    return [room_x1, room_x2, room_y1, room_y2, room_z1, room_z2, transmitter_xs, transmitter_ys, transmitter_zs, number_of_reflectances]