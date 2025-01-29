import networkx as nx
import matplotlib.pyplot as plt
import random

# numero de nós
eNe = 10000
#eNe = 4000
#eNe = 1000

# probabilidade fixa de conexão entre nós
Pe = 0.001
#Pe = 0.0004
#Pe = 0.0001
#lambda = eNe * Pe

eNe = 100
Pe = 0.2

# criar um grafo baseado em probalidade fixa de conexão
def gerar_grafo_aleatorio(n, p):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                G.add_edge(i, j)
                
    return G

G = gerar_grafo_aleatorio(eNe, Pe)

# desenhar o grafo
plt.figure(figsize=(6,6))
nx.draw (G, with_labels=True, node_color='lightblue' , edge_color= 'gray', node_size=500)
plt.title(f"Grafo Aleatorio com {eNe} Nós' (Pe={Pe})")
plt.show()

# criar o histograma do grau dos nós
graus = [d for n, d in G.degree()]
plt.figure(figsize=(6,4))
plt.hist(graus, bins=range(min(graus), max(graus) + 2), edgecolor='black', color='lightgreen')
plt.xlabel('Grau')
plt.ylabel('Frequência')
plt.title('Histograma do Grau de Nós')
plt.xticks(range(min(graus), max(graus) + 1))
plt.grid(axis='y' , linestyle='--', alpha=0.7)
plt.show()
