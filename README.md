# WikiMeter

## Concept Graph

### Execution
```bash
python3 main.py
python3 merge.py
python3 generate_networkx_graph.py
```

#### Input
To run your code, first put all the text files of your input into the input folder.

In **main.py** these parameters can be varied:  
1. max_window_size = 5
2. process_num = 12
3. min_count = 100
4. max_vocab_size = 100000
5. divisions = 6  

#### Pre-Processing
In **util.py**
```python
def preProcessing(input_raw_data_dir_name, processed_data_dir_name):
```
1. Conversion to small case.
2. Removing numbers, symbols and punctuations.
3. Stemming using Poster Stemmer.
4. Removing stop words.

#### Execution

After executing **main.py** runs directorywill be created with strucutre as follow:  
```bash
  | --- runs
        | --- run1
              | --- dicts_and_encoded_texts
              | --- edges
              | --- graph
              | --- input
              | --- processed
        | --- run2
              | --- dicts_and_encoded_texts
              | --- edges
              | --- graph
              | --- input
              | --- processed
        .
        .
        .
        .
        | --- run6
              | --- dicts_and_encoded_texts
              | --- edges
              | --- graph
              | --- input
              | --- processed
```
***run_i/dicts_and_encoded_texts/dict_merged.txt*** contains dictionary local to i-th run  
***run_i/dicts_and_encoded_texts/word_count_all.txt*** contains count of each word local to i-th run
***run_i/graph/encoded_edges_count_window_size_5.txt*** contains directed edge list local to i-th run.

#### Merging Outputs
To merge output(***dict_merged.txt*** and ***encoded_edges_count_window_size_5.txt***) of each run, execute **merge.py**. This will generate merged output in **merge** directory with below structure: 
```bash
   | --- merge
        | --- cummulative
              | --- dict1.pickle
              | --- dict2.pickle
              .
              .
              .
              | --- dict6.pickle
              | --- graph1.pickle
              | --- graph2.pickle
              .
              .
              .
              | --- graph6.pickle
        | --- dict.pickle
        | --- dict.txt
        | --- graph.pickle
        | --- graph.txt
```
Here starting from run_1, one output is merged at a time and output after each merge is stored in cumulative directory. Final merged graph and dictionary are stored both in .txt and .pickle format for fast reading.

#### Generate Networkx Graph
To generate a networkx graph, execute **generate_networkx_graph.py**. This will output a pickle file for our networkx graph, ***concept_graph.gpickle***.

## Concept Graph on Proper Nouns
Replace the **util.py** with **proper_nouns/util.py**

## Wikipedia Data
To get all the article's text data from wikipedia, run **wiki_xml_parser/wiki_extractor.py**, keep your xml file in same directory.
