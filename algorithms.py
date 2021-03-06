from functions import *
from drawing import show_weighted_grapgh, draw_subtree


def prims_algorithm(G, starting_vertex, show_graph = False, show_cost = False):
   #draw graph
   if show_graph == True:
       show_weighted_grapgh(G)
       
   T = prims_init(G, starting_vertex)
   #draw graph
   if show_graph == True:
       draw_subtree(G, T)
       
   while is_spanning(G, T) == False:
       e = min_cost_edge(G, T)
       T.add_edge(e[0],e[1])
       if show_graph == True:
           draw_subtree(G, T)
        #show cost
   if show_cost == True:
        c = sum[[cost(G, e) for e in V(T)]]
        print(f'The cost of this spanning tree is {c}')
   return T