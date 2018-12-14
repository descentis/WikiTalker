#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created: 25-10-2018
@author: pratik-chhajer
'''

from word_processing import *
from sentence_processing import *
from wordpair_processing import *
import util, multi_processing 
import time
import os

if __name__ == '__main__':
	
	''' Parameters of concept graph
		max_window_size : Maximum allowed window size of consideration
		process_num : Number of parallel threads running
		min_count : Minimum number of a times a word should occur in whole corpus to be considered as node.
		max_vocab_size : Maximum number of allowed nodes in graph, thresholding is done based on count.
		divisions : Number of divisions for input
	'''

	max_window_size = 5
	process_num = 12
	min_count = 100
	max_vocab_size = 100000
	divisions = 6


	safe_files_number_per_processor = 200
	start_time = time.time()

	input_folder = 'input'
	run_folder = 'runs'
	processed_folder = "processed"
	dicts_folder = "dicts_and_encoded_texts"
	edges_folder = "edges"
	graph_folder = "graph"

	flag = util.input(input_folder,run_folder,divisions,processed_folder,dicts_folder,edges_folder,graph_folder)

	if flag == -1 or flag == 0:
		exit()
		
	print('Created ' + str(flag) + ' divisions')


	for i in range(1,flag+1):

		processed = os.path.join('run_' + str(i),processed_folder)
		dicts = os.path.join('run_' + str(i),dicts_folder)
		edges = os.path.join('run_' + str(i),edges_folder)
		graph = os.path.join('run_' + str(i),graph_folder)

		processed = os.path.join(run_folder,processed)
		dicts = os.path.join(run_folder,dicts)
		edges = os.path.join(run_folder,edges)
		graph = os.path.join(run_folder,graph)

		curr_run_folder = os.path.join(run_folder,'run_' + str(i))

		input_folder = os.path.join(curr_run_folder,'input')

		if(os.path.isdir(run_folder + '/run_' + str(i) + '/processed') and len(os.listdir(run_folder + '/run_' + str(i) + '/processed')) > 0):
			print('run_' + str(i) + ' data is already processed, avoiding re-processing')
		else:
			print('processing input data of run_' + str(i))
			util.preProcessing(input_folder,processed)
		
		wp = WordProcessing(output_folder=dicts)
		merged_dict = wp.apply(data_folder=processed, process_num=process_num)
		sp = SentenceProcessing(dicts_folder=dicts, output_folder=edges,
								max_window_size=max_window_size, local_dict_extension='.dicloc')
		word_count_all = sp.apply(data_folder=dicts, process_num=process_num)
		wpp = WordPairsProcessing(max_vocab_size=max_vocab_size, min_count=min_count,
								  dicts_folder=dicts, window_size=max_window_size,
								  edges_folder=edges, graph_folder=graph,
								  safe_files_number_per_processor=safe_files_number_per_processor)
		result = wpp.apply(process_num=process_num)
		print('run_' + str(i) + ' completed, time in seconds:', util.count_time(start_time))