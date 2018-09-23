# -*- coding: utf-8 -*-
import sys
import yaml
from sys import argv
from pprint import pprint

def graph_parse(gfile):
    '''read graph from yaml file'''
    with open(gfile) as f:
            graph_dict = yaml.load(f)
    return graph_dict

def dfs(graph, start):
    '''depth-first search algorithm'''
    visited = []
    select = [start]
    while select:
        try:
            node = select.pop(0)
            if node not in visited:
	       #print('visited node -', node)
                visited = visited+[node]
                select = graph[node]+select
        except KeyError:
            print('Wrong graph, please check all node edges!')
            sys.exit()
           #print('====')
    return visited

def bfs(graph, start):
  '''breadth-first search algorithm'''
  visited = []
  select = [start]
  while select:
      try:
          node = select.pop(0)
          if not node in visited:
	     #print('visited node -', node)
              visited = visited+[node]
              select = select+graph[node]
      except KeyError:
            print('Wrong graph, please check all node edges!')
            sys.exit()
 #print('====')
  return visited


#Input parameters section
input_file = ''.join(argv[1:2])
start_node = ''.join(argv[2:3])

if not input_file or not start_node:
    print('Missing input parameters!')
    print('Usage should be: python graph.py <filename>.yaml <start_node>')
    sys.exit()
    
if __name__ == '__main__':
    print('Converted input graph: ')
    pprint(graph_parse(input_file))
    print('Visited nodes in depth --', dfs(graph_parse(input_file), start_node))
    print('Visited nodes in breadth --', bfs(graph_parse(input_file), start_node))
