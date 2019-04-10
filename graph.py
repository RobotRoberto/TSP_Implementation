from tsputils import dist

"""
A generic Graph class that builds from the basic library with intentions
to help modularize the code for building the TSP Solver, it supports
several file types ranging from the test files from class to TSPLIB format.
"""
class Graph:
    def __init__(self):
       self.nodes = [0]
       self.coordinates = {0: (0,0)}
       self.nodes_not_visited = set()
       self.edges = None

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
                self.nodes.append(node)

        self.edges = [[dist(self.coordinates[node], self.coordinates[neighbor])
            for neighbor in self.nodes] for node in self.nodes]
    """
    Helper method useful in debugging sessions or for display in enjoyment
    """
    def display(self):
        print("This graph has the following nodes:", list(self.nodes))
        print("And, coordinates of the graph nodes are:",
               self.coordinates)
        print(self.edges)


    def get_nodes(self):
        return self.nodes[1:]
