import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([('Asj', 'Dfa')])
G.add_edges_from([('Bsa', 'Das')])
G.add_edges_from([('Bsa1', 'Das')])
G.add_edges_from([('Bsa2', 'Das')])
G.add_edges_from([('Bsa3', 'Das')])
G.add_edges_from([('Bsa4', 'Das')])
G.add_edges_from([('Bsa5', 'Das')])
G.add_edges_from([('Bsa6', 'Das')])


plt.figure(figsize=(10, 10))
nx.draw_networkx(G, with_labels=True)

hubs, authorities = nx.hits(G, max_iter=50, normalized=True)
# The in-built hits function returns two dictionaries keyed by nodes
# containing hub scores and authority scores respectively.

print("Hub Scores: ", hubs)
print("Authority Scores: ", authorities)