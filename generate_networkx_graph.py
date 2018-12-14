import networkx as nx
import numpy as np
import time
import os


if __name__ == '__main__':

	merge_folder = "merge"

	graph = os.path.join(merge_folder,'graph.txt')

	start = time.clock()

	E = []
	s = 0
	with open(graph, "r") as file:
		for line in file:
			L = line[:-1]
			L = L.split('\t')
			if len(L) == 3:
				E.append((int(L[0]),int(L[1]),int(L[2])))
				s += int(L[2])
			else:
				break

	s /= len(E)
	t = s
	print('Average count', s)
	print('time taken so far:', time.clock() - start)

	Nodes = set()
	for i in E:
		Nodes.add(i[0])
		Nodes.add(i[1])
	Nodes = list(Nodes)
	print('nodes list created')
	print('number of nodes', len(Nodes))
	print('time taken so far:', time.clock() - start)

	G = nx.DiGraph()
	G.add_nodes_from(Nodes)
	print('nodes added')
	for i in E:
		G.add_edge(i[0],i[1],weight=i[2])
	print('edges added')
	print('time taken so far:', time.clock() - start)

	nx.write_gpickle(G,"concept_graph"+".gpickle")
	print('time taken so far:', time.clock() - start)
