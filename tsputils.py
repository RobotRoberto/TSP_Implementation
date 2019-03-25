import math

"""
A utility function to figure out the euclidean distance between two nodes
"""
def dist(node1, node2):
    return math.sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)
