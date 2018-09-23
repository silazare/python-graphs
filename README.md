## Graph search algoritms script

[![Build status](https://travis-ci.org/silazare/python-graphs.svg?master)](https://travis-ci.org/silazare)

This script is prepared for undirected graph visiting round.
Expected input is an undirected graph and node from which we should start to search.
Some graph examples are attached.

#### Usage description:
```sh
$ python3 graph.py <filename>.yml <start_node>
```
Where <filename>.yml - is YAML structured file format with graph description
<start_node> - is node name from which we should start to search

#### Functions description:
`graph_parse(gfile)` - read and convert graph from input YAML file to dictionary

**gfile** - input file in YAML format with dict file structure, where nodes are Keys and all edges from the node are list Items.
Each node must have all its edges defined.
Output returns dictionary with nodes and edges.

`dfs(graph, start)` - depth-first search algorithm for graph.

**graph** - input graph in dict format with nodes and edges.
**start** - start node from which search should be started.
Output returns visited nodes list, order is according DFS algorithm.

`bfs(graph, start)` - breadth-first search algorithm for graph.

**graph** - input graph in dict format with nodes and edges.
**start** - start node from which search should be started.
Output returns visited nodes list, order is according BFS algorithm.


Example structure:

Graph>
 ```        
         A
       /   \
      B--D--C
       \ | /
         E
```
Input file structure>
```
A:
- B
- C

B:
- A
- D
- E

C:
- A
- D
- E

D:
- B
- C
- E

E:
- B
- C
- D
```
