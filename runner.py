import modified_monte_carlo_algorithm
import random_generator
import output_handler
import random
import sys
import json
import time

max_room_size = 4
parameters = []
draw_chart = True
number_of_input_values = 1

for i in range(number_of_input_values):
    single_simulation_parameters = random_generator.generate_random_input_values(max_room_size)
    single_channel_impulse_response = modified_monte_carlo_algorithm.compute(single_simulation_parameters, draw_chart)
    parameters.append(single_simulation_parameters + single_channel_impulse_response)
    print(i) 

file_name = "deep_neural_network_input.xlsx"
output_handler.save(file_name, parameters) 
