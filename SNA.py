# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import networkx as nx
import matplotlib.pyplot as plt

# <codecell>

Gws = nx.connected_watts_strogatz_graph(50,6,0.3)

# <codecell>

nx.draw_circular(Gws)
plt.show()

# <codecell>

Gba = nx.barabasi_albert_graph(150,4)

# <codecell>

nx.draw_spring(Gba)
plt.show()

# <codecell>

karate = nx.karate_club_graph()

# <codecell>

nx.draw_spring(karate)
plt.show()

# <codecell>

nameyears = {}
fh = open('booknames.csv','r+')
for line in fh:
    year,names,freq = line.split(',')
    name1,name2=names.split('-')
    if year in nameyears:
        if name1<name2:
            if name1 in nameyears[year]:
                if name2 in nameyears[year][name1]:
                    nameyears[year][name1][name2] += freq
                else:
                    nameyears[year][name1][name2] = freq
            else:
                nameyears[year][name1]={name2:freq}
        else:
            if name2 in nameyears[year]:
                if name1 in nameyears[year][name2]:
                    nameyears[year][name2][name1] += freq
                else:
                    nameyears[year][name2][name1] = freq
            else:
                nameyears[year][name2]={name1:freq}
    else:
        if name1<name2:
            nameyears[year]={name1:{name2:freq}}
        else:
            nameyears[year]={name2:{name1:freq}}

# <codecell>

nameyears[2000]

# <codecell>

graphyears = {}
for year, names in graphyears:
    G = nx.Graph()
    for node, neighbors in names:
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    graphyears[year] = G

# <codecell>

G2000 = graphyears[2000]

# <codecell>

nx.draw_spring(G2000)
plt.show()

# <codecell>

G2000.degree('michael')

# <codecell>

nx.write_adjlist(karate, 'karateclub_adj.csv')

# <codecell>

for edge in nx.edges_iter(karate):
    print edge

# <codecell>

karate_json = {"nodes":[],"links":[]}
for node in nx.nodes_iter(karate):
    n = {"name":node, "group":1}
    karate_json["nodes"].append(n)
for edge in nx.edges_iter(karate):
    e = {"source":edge[0], "target":edge[1], "value":1}
    karate_json["links"].append(e)

# <codecell>

print karate_json

# <codecell>

import json
fh = open('karate.json','w')
json.dump(karate_json, fh)
fh.close()

# <codecell>


