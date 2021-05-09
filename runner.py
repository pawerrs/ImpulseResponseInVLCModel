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
number_of_input_values_per_serie = 1
number_of_series = 1

file_name = "neural_network_input3000.xlsx"

for k in range(number_of_series):
    for i in range(number_of_input_values_per_serie):
        single_simulation_parameters = random_generator.generate_random_input_values(max_room_size)
        single_channel_impulse_response = modified_monte_carlo_algorithm.compute(single_simulation_parameters, draw_chart)
        parameters.append(single_simulation_parameters + single_channel_impulse_response)
        print(str(k) + ": " + str(i)) 

    output_handler.save(file_name, parameters) 
