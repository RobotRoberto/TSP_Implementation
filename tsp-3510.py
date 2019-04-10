import networkx as nx
import graph
import math
from graph import Graph
import heapq as hq
import time
from tsputils import swap, calculate_tour_dist, tsp_simulated_annelling
from tsputils import read_opt_tour, tsp_2opt, swap
import random

start = time.time()
graph = Graph()
graph.populate_from_file('dataset/pcb442.txt')
# opt_tour = read_opt_tour('dataset/pcb442-opt.txt')

tour = graph.get_nodes()
tour.append(tour[0])

print("The random tour is: ", tour)
print(f'Distance of tour: {calculate_tour_dist(graph, tour)}')

tour = tsp_simulated_annelling(graph, tour, 200, time.time()+90)
# while time.time() < start + 180:
#      tour = run_2opt(graph, tour, time.time()+22)
#      tour = simulated_annelling_tsp(graph, tour, 50, time.time()+22)
tour = tsp_2opt(graph, tour, time.time()+90)

if time.time() < start + 180:
    tour = tsp_simulated_annelling(graph, tour, 30, start + 180)

print("The tour is: ", tour)
print(f'Distance of tour: {calculate_tour_dist(graph, tour)}')
print("Total execution time:" + str(time.time()-start))
# print("The optimal tour is:", opt_tour)
# print(f'Distance of opt tour is: {calculate_tour_dist(graph, opt_tour)}')
