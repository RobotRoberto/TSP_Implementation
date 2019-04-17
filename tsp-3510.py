import graph
import math
from graph import Graph
import heapq as hq
import time
from tsputils import swap, calculate_tour_dist, tsp_simulated_annelling
from tsputils import read_opt_tour, tsp_2opt, swap, tsp_simulated_annelling_mod
import random
from argparse import ArgumentParser

parser = ArgumentParser(description="\tMy TSP Solver and Implementation.\n\n")
parser.add_argument('-i', '--input', help='\t\tInput file for TSP graph.',
    type=str, required=True)
parser.add_argument('-o', '--output', help='\t\tOutput file for the solution.',
    type=str, required=True)
parser.add_argument('-t', '--time', help='\t\tTime to run the application.',
    type=int, required=True)
args = parser.parse_args()

start, time_to_complete = time.time(), args.time
file_in, file_out = args.input, args.output
graph = Graph()
graph.populate_from_file(file_in)

tour = graph.get_nodes()
tour.append(tour[0])

print("The random tour is: ", tour)
print(f'Distance of tour: {calculate_tour_dist(graph, tour)}')

h_time = time_to_complete / 2
critical_time = 2
q_time = ((h_time - critical_time) / 2)
stop_time = start + time_to_complete - critical_time

tour = tsp_simulated_annelling(graph, tour, 200, time.time()+h_time)
while time.time() < stop_time:
      tour = tsp_2opt(graph, tour, time.time()+q_time)
      tour = tsp_simulated_annelling_mod(graph, tour, 50, time.time()+q_time)

print("The tour is: ", tour)
print(f'Distance of tour: {calculate_tour_dist(graph, tour)}')
print("Total execution time:" + str(time.time()-start))

with open(file_out, "w") as file:
    for node in tour:
        file.write(str(node) + "\n")

print("Finished running application.")
