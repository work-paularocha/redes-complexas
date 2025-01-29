import pylab
import matplotlib 
import networkx as nx

G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)
nx.draw(G)
pylab.show()