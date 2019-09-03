#!/usr/bin/env python3
import networkx as nx
from csv import DictReader
import sys, json, os.path

DATA_DIR=os.path.dirname(os.path.abspath(__file__))
PUBS=os.path.join(DATA_DIR, 'wos-extract.cleaned-coauthornet.for-sci2.csv')
OUT=os.path.join(DATA_DIR, 'wos-extract.cleaned-coauthornet.for-gephi.graphml')
METADATA=os.path.join(DATA_DIR, 'extra-author-metadata.json')
SPLIT_ON='|'
TC_FIELD='Times Cited'
AUTHORS_FIELD='Authors'

if len(sys.argv) > 1:
  PUBS=sys.argv[1]

metadata = {}
if os.path.exists(METADATA):
  metadata = json.load(open(METADATA))
  print(metadata)

G = nx.Graph()
with open(PUBS) as in_f:
  for row in DictReader(in_f):
    authors, numCites = row[AUTHORS_FIELD].split(SPLIT_ON), int(row.get(TC_FIELD, 0))
    authors.sort()

    for a in authors:
      if G.has_node(a):
        node = G.nodes[a]
        node['number_of_authored_works'] += 1
        node['times_cited'] += numCites
      else:
        extra_md = metadata.get(a, {})
        extra_md['show_label'] = extra_md.get('show_label', False)

        G.add_node(a, number_of_authored_works=1, times_cited=numCites, **extra_md)

    for source in range(len(authors)):
      a1 = authors[source]
      for target in range(source + 1, len(authors)):
        a2 = authors[target]
        if a1 != a2:
          if G.has_edge(a1, a2):
            edge = G.edges[a1, a2]
            edge['number_of_coauthored_works'] += 1
            edge['times_cited'] += numCites
          else:
            G.add_edge(a1, a2, number_of_coauthored_works=1, times_cited=numCites)

def remove_edges():
  to_remove = []
  for a1,a2, attr in G.edges(data = True):
    if attr['number_of_coauthored_works'] <= 2:
      to_remove.append((a1, a2))
  G.remove_edges_from(to_remove)
  print(len(to_remove))

  to_remove = []
  for n, attr in G.nodes(data = True):
    if G.degree(n) == 0:
      to_remove.append(n)

  G.remove_nodes_from(to_remove)
  print(len(to_remove))

print(f'Nodes: {len(G.nodes)}\nEdges: {len(G.edges)}')
print(f'Writing network file to:\n\t{OUT}')
nx.write_graphml(G, OUT)
