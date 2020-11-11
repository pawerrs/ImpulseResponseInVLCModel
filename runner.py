import mmc_algorithm
import random_generator
import results_saver
import random
import sys
import json

max_room_size = 4
parameters = []

number_of_input_values = 200
for i in range(number_of_input_values):
    single_simulation_parameters = random_generator.generate_random_input_values(max_room_size)
    single_channel_impulse_response = mmc_algorithm.solve(single_simulation_parameters)
    parameters.append(single_simulation_parameters + single_channel_impulse_response)
    print(i) 

file_name = "deep_neural_network_input.xlsx"
results_saver.save(file_name, parameters) 