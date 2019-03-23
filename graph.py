import networkx as nx

"""
A generic Graph class that builds from networkx library with intentions
to help modularize the code for building the TSP Solver, it supports 
several file types ranging from the test files from class to TSPLIB format.
"""
class Graph:
    def __init__(self):
       self.G = nx.Graph()
       self.coordinates = {}

    """
    A method to use for populating the graph with nodes from the datasets,
    and the populating method will differ with different type of format.
    """
    def populate_from_file(self, file_name, file_type='test_from_class'):
        with open(file_name) as graph_file:
            for line in graph_file:
                data = line.rstrip('\n')
                data = data.split()
                node = int(data[0]) 
                self.coordinates[node] = (float(data[1]), float(data[2]))
                self.G.add_node(node)

    """
    Helper method useful in debugging sessions or for display in enjoyment
    """
    def display(self):
        print("This graph has the following nodes:", list(self.G))
        print("This graph has the following edges:", list(self.G))
        print("And, coordinates of the graph nodes are:",
               self.coordinates)
