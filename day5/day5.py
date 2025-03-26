import os
from collections import defaultdict

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    rules = []
    updates = []
    parsing_rules = True
    
    for line in lines:
        if '|' in line:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
        else:
            updates.append(list(map(int, line.split(','))))
    
    return rules, updates

def build_dependency_graph(rules):
    graph = defaultdict(set)
    for x, y in rules:
        graph[x].add(y)
    return graph

def is_valid_order(update, graph):
    index_map = {num: idx for idx, num in enumerate(update)}
    for x in update:
        for y in graph.get(x, set()):
            if y in index_map and index_map[x] > index_map[y]:
                return False
    return True

def find_middle_value(update):
    return update[len(update) // 2]

def main(file_path):
    rules, updates = parse_input(file_path)
    graph = build_dependency_graph(rules)
    
    valid_middle_values = [find_middle_value(update) for update in updates if is_valid_order(update, graph)]
    return sum(valid_middle_values)

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "text.txt")
    result = main(file_path)
    print("Sum of middle page numbers of valid updates:", result)
