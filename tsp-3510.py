import networkx as nx
import graph
import math
from graph import Graph
import heapq as hq

graph = Graph()
graph.populate_from_file('dataset/mat-test.txt')

inf = float("inf")
src = 1

dist = graph.edges[src]
print(dist)
path = []
queue = []
hq.heappush(queue, (dist[src], src))
last_node = src
total_dist = 0

while len(queue) > 0:
    node_dist, node = hq.heappop(queue)

    if node not in graph.unvisited_nodes():
        continue

    graph.visit(node)
    path.append(node)
    total_dist += graph.edges[last_node][node]
    last_node = node
    print("Visiting node ", node)
    print(total_dist)

    for neighbor in graph.unvisited_nodes():
        if graph.edges[node][neighbor] <= dist[neighbor]:
            new_dist = graph.edges[node][neighbor]
            dist[neighbor] = new_dist
            hq.heappush(queue, (new_dist, neighbor))
    
    print(dist)
    print("***********************")
    print("***********************")
    print("***********************")

# Getting back to the source
# path.append(src)
# total_dist += graph.edges[last_node][src]

            
print("The two-approximation algorithm for the TSP Solver yields: ", total_dist)
print("The path is: ", path)
print(sum(dist)-dist[0])
