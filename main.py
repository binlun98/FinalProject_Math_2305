import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *



#user input the graph, asks if they want show cost/graph
graph_data = open('test_graph/G1.txt','r')
# G = graph, T = vertercies
G = nx.read_weighted_edgelist(graph_data, nodetype=int)
T = prims_algorithm(G, 0, True, True)

