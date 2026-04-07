import networkx as nx 

Th = 3
G = nx.DiGraph()
F = open('/Users/sr0215/Python/Social/email-enron-only.mtx', 'r')

for l in F.readlines():

    # if len(l.split(' ')) != 3:
    #     continue

    # u, v, w = l.split(' ')
    u, v = l.split(' ')
    u = int(u)
    v = int(v)

    if u == v:
        continue

    # if not G.has_edge(v, u):
    G.add_edge(u, v)
    print(u, v, max(list(G.nodes())))

G.remove_nodes_from(nx.isolates(G))

G = nx.convert_node_labels_to_integers(G, first_label = 0)
print (G)

nx.write_gml(G, 'Email_Now.gml')