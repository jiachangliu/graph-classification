import networkx as nx
from data_utils import read_graphfile
import numpy as np
import sys

def preprocess(DS):
    graphs = read_graphfile('../data', DS)
    lab = open('../data/{}_label.txt'.format(DS), 'w')
    f = open('../data/{}.txt'.format(DS), 'w')
    nl = open('../data/{}_nodelabels.txt'.format(DS), 'w')
    f.write('{}\n'.format(len(graphs)))
    nl.write('{}\n'.format(len(graphs)))

    for g in graphs:
        num_nodes = g.number_of_nodes()
        f.write('{}\n'.format(num_nodes))
        nl.write('{}\n'.format(num_nodes))
        lab.write('{}\n'.format(g.graph['label']))

        A = np.array(nx.adjacency_matrix(g).todense())
        assert A.shape == (num_nodes, num_nodes)
        for u in g.nodes():

            f.write(' '.join(list(map(str, list(A[int(u)])))) + '\n')
            try:
                # nl.write('{}\n'.format(np.argmax(g.node[int(u)]['label'])+1))
                nl.write('{}\n'.format(np.argmax(g.nodes[int(u)]['label'])+1))
            except:
                print("goes here")
                pass
        
    f.close()
    nl.close()
    lab.close()

if __name__ == '__main__':
    # x, y = get_mutag()
    # evaluate_embedding(x, y)
    import sys
    preprocess(sys.argv[1])
