from collections import defaultdict
import networkx as nx


with open('inputs/input_day12.txt') as f:
    lines = f.read().splitlines()

def solve_p1(graph, path=['start']):
    currrent = path[-1]
    paths = []
    for n in graph.neighbors(currrent):
        new_path = path + [n]
        if n == 'end':
            yield new_path
        elif n.isupper() or n not in path:
            yield from solve_p1(graph, new_path)


graph = nx.Graph()
for line in lines:
    graph.add_edge(*line.split('-'))

print(len([i for i in solve_p1(graph)]))

### Part Two ###
def solve_p2(graph, path=['start'], doubles=False):
    currrent = path[-1]
    for n in graph.neighbors(currrent):
        new_path = path + [n]
        if n == 'end':
            yield new_path
        elif n.isupper() or n not in path:
            yield from solve_p2(graph, new_path, doubles=doubles)
        elif doubles and n != 'start' :
            yield from solve_p2(graph, new_path, doubles=False)

print(len([path for path in solve_p2(graph, doubles=True)]))