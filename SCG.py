import networkx as nx
import math

def strongRelation(n, m):
    G = nx.Graph()
    p = math.ceil(m / n)
    edges_m = []
    for j in range(p):
        for i in range(n):
            if m > 0:
                if i + j >= n - 1:
                    edges_m.append((i, i + j + 1 - n))
                else:
                    edges_m.append((i, i + j + 1))
                m = m - 1

    G.add_edges_from(edges_m)
    cliques = nx.find_cliques(G)
    cliques1 = [clq for clq in cliques]

    return max([len(i) for i in cliques1])

strongRelation(5, 10) #example
