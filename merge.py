import os
import pickle

if __name__ == '__main__':

	max_window_size = 5
	run_folder = 'runs'
	divisions = 6
	dicts_folder = "dicts_and_encoded_texts"
	graph_folder = "graph"
	merge_folder = "merge"

	if os.path.isdir(merge_folder) is False:
		os.mkdir(merge_folder)
		os.mkdir(os.path.join(merge_folder,'cummulative'))

	cummulative = os.path.join(merge_folder,'cummulative')


	curr_path = os.path.join(run_folder,'run_1')
	
	dict_path = os.path.join(curr_path,dicts_folder)
	dict_path = os.path.join(dict_path,'dict_merged.txt')

	graph_path = os.path.join(curr_path,graph_folder)
	graph_path = os.path.join(graph_path,'encoded_edges_count_window_size_' + str(max_window_size) + '.txt')

	Dictionary = {}
	with open(dict_path, "r") as file:
		for line in file:
			L = line[:-1]
			L = L.split('\t')
			if len(L) == 2:
				Dictionary[L[0]] = int(L[1])

	Edges = {}
	with open(graph_path, "r") as file:
		for line in file:
			L = line[:-1]
			L = L.split('\t')
			if len(L) == 3:
				Edges[(int(L[0]),int(L[1]))] = int(L[2])

	print('run_1 dict and graph reading done')

	for i in range(2,divisions+1):
		curr_path = os.path.join(run_folder,'run_'+str(i))
		
		dict_path = os.path.join(curr_path,dicts_folder)
		dict_path = os.path.join(dict_path,'dict_merged.txt')

		graph_path = os.path.join(curr_path,graph_folder)
		graph_path = os.path.join(graph_path,'encoded_edges_count_window_size_' + str(max_window_size) + '.txt')


		Id2Id = {}
		with open(dict_path, "r") as file:
			for line in file:
				L = line[:-1]
				L = L.split('\t')
				if len(L) == 2:
					if L[0] in Dictionary:
						Id2Id[int(L[1])] = Dictionary[L[0]]
					else:
						Id2Id[int(L[1])] = len(Dictionary)
						Dictionary[L[0]] = len(Dictionary)

		with open(graph_path, "r") as file:
			for line in file:
				L = line[:-1]
				L = L.split('\t')
				if len(L) == 3:
					a = Id2Id[int(L[0])]
					b = Id2Id[int(L[1])]
					c = int(L[2])
					if (a,b) in Edges:
						Edges[(a,b)] += c
					else:
						Edges[(a,b)] = c

		with open(os.path.join(cummulative,'dict' + str(i) + '.pickle'), 'wb') as handle:
			pickle.dump(Dictionary,handle)

		print('run_' + str(i) + ' dict dumped')

		with open(os.path.join(cummulative,'graph' + str(i) + '.pickle'), 'wb') as handle:
			pickle.dump(Edges,handle)

		print('run_' + str(i) + ' graph dumped')


	with open(os.path.join(merge_folder,'dict.pickle'),'wb') as handle:
		pickle.dump(Dictionary,handle)

	print('Dict dumped!')

	with open(os.path.join(merge_folder,'graph.pickle'),'wb') as handle:
		pickle.dump(Edges,handle)

	print('Graph dumped!')


	with open(os.path.join(merge_folder,'dict.txt'), 'a') as out:
		for key, val in Dictionary.items():
			out.write(key + '\t' + str(val) + '\n')

	with open(os.path.join(merge_folder,'graph.txt'), 'a') as out:
		for key, val in Edges.items():
			out.write(str(key[0]) + '\t' + str(key[1]) + '\t' + str(val) + '\n')