import networkx as nx

#show set of vertercies
def V(graph):
    return set(graph.nodes())
#show set of edges
def E(graph):
    return set(graph.nodes())
#creat graph

def prims_init(graph, v):
    if v not in V(graph):
        return "Enter vertex not found"
    else: 
        T = nx.Graph()
        T.add_node(v)
        return T 
    
#check if the is the is still spanning
def is_spanning(graph, subgraph):
    return V(graph) == V(subgraph)

#return cost of the edge
def cost(G, e):
    return G[e[0]][e[1]]['weight']

#merging/union edges that is duplicated
def possible_edges(G, T):
    return [e for e in list(G.edges(V(T))) if e[0] not in V[T] or e[1] not in V(T)]

#sort() // temp_edge.sort() = (44:47)
def min_prims_edge(g):
    copy = g.sort(key = lambda e : cost(G, e))
    return g 
