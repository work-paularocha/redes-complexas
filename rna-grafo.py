import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo completo com 10 nós
G = nx.complete_graph(10)

# Desenhando o grafo
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_size=500, node_color="lightblue", font_size=12, font_weight="bold", edge_color="gray")
plt.title("Rede com 10 Nós (Grafo Completo)")
plt.show()
