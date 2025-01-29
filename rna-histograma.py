#faça uma representação gráfica dessa rede
#prompt
# Mantenha as funcionalidades anteriores e acrescente um histograma do grau da rede (rna-grafo)

import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo completo com 10 nós
G = nx.complete_graph(10)

# Desenhando o grafo
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_size=500, node_color="lightblue", font_size=12, font_weight="bold", edge_color="gray")
plt.title("Rede com 10 Nós (Grafo Completo)")
plt.show()

# Calculando os graus dos nós
graus = [G.degree(n) for n in G.nodes()]

# Plotando o histograma do grau
plt.figure(figsize=(8, 6))
plt.hist(graus, bins=range(min(graus), max(graus) + 2), edgecolor='black', color='lightgreen')
plt.title("Histograma do Grau da Rede")
plt.xlabel("Grau")
plt.ylabel("Frequência")
plt.grid(True)
plt.show()

