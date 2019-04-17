import math
import random
import time
import gc

"""
A utility function to figure out the euclidean distance between two nodes
"""
def dist(node1, node2):
    return math.sqrt(math.pow(node1[0]-node2[0], 2) + math.pow((node1[1]-node2[1]),2))

def read_opt_tour(file_name):
    with open(file_name) as graph_file:
        tour = []
        for line in graph_file:
            data = line.rstrip('\n')
            data = data.split()
            node = int(data[0])
            tour.append(node)

        return tour

def calculate_tour_dist(graph, tour):
    start = tour[0]
    dist = 0
    prev = start

    for i in range(1, len(tour)):
        curr = tour[i]
        dist += graph.edges[prev][curr]
        prev = curr

    return dist

def swap(tour, i, k):
    new_tour = tour[0:i+1] + tour[k:i:-1] + tour[k+1::]
    assert(len(new_tour) == len(tour))
    return new_tour

def temperature_function(curr_tour_dist, potential_tour_dist, temperature):
    delta = potential_tour_dist - curr_tour_dist
    probability = math.exp((-1 * delta) / temperature)

    return random.uniform(0,1) <= probability

def same_tour(tour1, tour2):
    if len(tour1) == len(tour2):
        for i in range(len(tour1)):
            if tour1[i] != tour2[i]:
                return False

        return True
    else:
        return False

def temperature_schedule(temperature, iterations_since_swap):
    if temperature <= 30:
        if iterations_since_swap > 2800:
            return 200
        else:
            return temperature + 0.05
    else:
        return temperature - 0.05

def tsp_simulated_annelling(graph, tour, temperature, stopping_time):
    print("Simulated Annealing")
    curr_cost = calculate_tour_dist(graph, tour)

    global_best_tour, best_tour_cost = tour, curr_cost
    itr_since_swp = 0
    while time.time() < stopping_time:
        i = random.randint(1, len(tour)-3)
        k = random.randint(i+1, len(tour)-2)

        if (k-i) == 1:
            continue

        new_tour = swap(tour, i, k)

        if time.time() > stopping_time:
            break

        new_tour_cost = calculate_tour_dist(graph, new_tour)

        if time.time() > stopping_time:
            break

        if new_tour_cost < curr_cost:
            tour, curr_cost = new_tour, new_tour_cost
            itr_since_swp = 0

            if time.time() > stopping_time:
                break

            if new_tour_cost < best_tour_cost:
                global_best_tour, best_tour_cost = tour, curr_cost
        elif temperature_function(curr_cost, new_tour_cost, temperature):
            itr_since_swp = 0
            tour, curr_cost = new_tour, new_tour_cost
        else:
            itr_since_swp += 1

        temperature = temperature_schedule(temperature, itr_since_swp)

    return global_best_tour

def tsp_2opt(graph, route, stopping_time):
    print("TWO OPT")
    improvement = True
    best_route = route
    best_distance = calculate_tour_dist(graph, route)
    while improvement and time.time() < stopping_time:
        improvement = False
        for i in range(1, len(best_route) - 2):

            if time.time() > stopping_time:
                break

            for k in range(i+1, len(best_route)-1):
                if (k-i) == 1:
                    continue

                if time.time() > stopping_time:
                    break

                new_route = swap(best_route, i, k)
                new_distance = calculate_tour_dist(graph, new_route)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_route = new_route
                    improvement = True

    assert len(best_route) == len(route)
    return best_route

def random_set(length):
    r_set = set()
    for i in range(1, length-2):
        for j in range(i+1, length-1):
            r_set.add((i,j))

    return r_set

def tsp_simulated_annelling_mod(graph, tour, temperature, stopping_time):
    print("Modified Simulated Annealing")
    curr_cost = calculate_tour_dist(graph, tour)

    global_best_tour, best_tour_cost = tour, curr_cost
    curr_set = random_set(len(tour))
    itr_since_swp = 0
    while time.time() < stopping_time:
        if len(curr_set) == 0:
            curr_set = random_set(len(tour))

        outcome = random.sample(curr_set, 1)
        i, k = outcome[0]

        new_tour = swap(tour, i, k)

        if time.time() > stopping_time:
            break

        new_tour_cost = calculate_tour_dist(graph, new_tour)

        if time.time() > stopping_time:
            break

        if new_tour_cost < curr_cost:
            tour, curr_cost = new_tour, new_tour_cost
            itr_since_swp = 0

            if time.time() > stopping_time:
                break

            if new_tour_cost < best_tour_cost:
                global_best_tour, best_tour_cost = tour, curr_cost
        elif temperature_function(curr_cost, new_tour_cost, temperature):
            itr_since_swp = 0
            tour, curr_cost = new_tour, new_tour_cost
        else:
            itr_since_swp += 1
            curr_set.remove((i, k))

        temperature = temperature_schedule(temperature, itr_since_swp)

    return global_best_tour
