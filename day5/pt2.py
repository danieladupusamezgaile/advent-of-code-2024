import os
from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    rules = []
    updates = []
    
    for line in lines:
        if '|' in line:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
        else:
            updates.append(list(map(int, line.split(','))))
    
    return rules, updates

def build_dependency_graph(rules):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    
    for x, y in rules:
        graph[x].add(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0
    
    return graph, in_degree

def is_valid_order(update, graph):
    index_map = {num: idx for idx, num in enumerate(update)}
    for x in update:
        for y in graph.get(x, set()):
            if y in index_map and index_map[x] > index_map[y]:
                return False
    return True

def find_middle_value(update):
    if not update:  # Check if the list is empty
        return None  # Or raise an exception, depending on how you want to handle it
    return update[len(update) // 2]

import heapq

def topological_sort(subset, graph, in_degree):
    """Perform a topological sort and return the ordered list."""
    sub_graph = {key: set(value) for key, value in graph.items() if key in subset}
    sub_in_degree = {key: in_degree[key] for key in subset}
    
    # Min-heap (priority queue) to process nodes in the correct order
    queue = []
    for node in subset:
        if sub_in_degree[node] == 0:
            heapq.heappush(queue, -node)  # Use negative values for max-heap behavior
    
    sorted_list = []
    
    while queue:
        node = -heapq.heappop(queue)  # Retrieve max value (since we stored negative values)
        sorted_list.append(node)
        
        for neighbor in sub_graph.get(node, []):
            sub_in_degree[neighbor] -= 1
            if sub_in_degree[neighbor] == 0:
                heapq.heappush(queue, -neighbor)
    
    return sorted_list


def main(file_path):
    rules, updates = parse_input(file_path)
    graph, in_degree = build_dependency_graph(rules)
    
    valid_middle_values = []
    fixed_middle_values = []
    
    for update in updates:
        if is_valid_order(update, graph):
            middle_value = find_middle_value(update)
        if middle_value is not None:
            valid_middle_values.append(middle_value)
        else:
            sorted_update = topological_sort(set(update), graph, in_degree)
            middle_value = find_middle_value(sorted_update)
        if middle_value is not None:
            fixed_middle_values.append(middle_value)

    
    print("Sum of middle page numbers of valid updates:", sum(valid_middle_values))
    print("Sum of middle page numbers of fixed updates:", sum(fixed_middle_values))

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "text.txt")
    main(file_path)