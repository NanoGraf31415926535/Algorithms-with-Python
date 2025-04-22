from collections import deque
import heapq

def breadth_first_search(graph, start_node):
    """Performs Breadth-First Search and returns visited nodes in order."""
    visited = []
    queue = deque([start_node])
    visited.append(start_node)
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

def depth_first_search(graph, start_node, visited=None):
    """Performs Depth-First Search and returns visited nodes in order."""
    if visited is None:
        visited = []
    visited.append(start_node)
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)
    return visited

def dijkstra(graph, start_node):
    """Finds the shortest paths from start_node to all other nodes in a weighted graph."""
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def prim(graph):
    """Finds the Minimum Spanning Tree of a weighted undirected graph."""
    mst = {}
    visited = set()
    start_node = next(iter(graph))  # Pick an arbitrary starting node
    visited.add(start_node)
    priority_queue = []

    for neighbor, weight in graph.get(start_node, {}).items():
        heapq.heappush(priority_queue, (weight, start_node, neighbor))

    while priority_queue:
        weight, u, v = heapq.heappop(priority_queue)
        if v not in visited:
            visited.add(v)
            mst[(u, v)] = weight
            for neighbor, w in graph.get(v, {}).items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (w, v, neighbor))

    return mst

def topological_sort(graph):
    """Performs topological sort on a Directed Acyclic Graph (DAG)."""
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph.get(node, []):
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    sorted_list = []

    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_list) == len(graph):
        return sorted_list
    else:
        return "Graph has a cycle"

# Example Usage:
if __name__ == "__main__":
    # Unweighted graph for BFS and DFS
    unweighted_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("BFS:", breadth_first_search(unweighted_graph, 'A'))
    print("DFS:", depth_first_search(unweighted_graph, 'A'))

    # Weighted graph for Dijkstra's
    weighted_graph_dijkstra = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'D': 5, 'E': 1},
        'C': {'A': 2, 'F': 1},
        'D': {'B': 5, 'E': 3},
        'E': {'B': 1, 'D': 3, 'F': 2},
        'F': {'C': 1, 'E': 2}
    }

    print("Dijkstra from A:", dijkstra(weighted_graph_dijkstra, 'A'))

    # Weighted undirected graph for Prim's
    weighted_undirected_graph_prim = {
        'A': {'B': 2, 'D': 1},
        'B': {'A': 2, 'C': 3, 'D': 3},
        'C': {'B': 3, 'E': 4},
        'D': {'A': 1, 'B': 3, 'E': 5},
        'E': {'C': 4, 'D': 5}
    }

    print("Prim's MST:", prim(weighted_undirected_graph_prim))

    # Directed Acyclic Graph for Topological Sort
    dag = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D', 'E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }

    print("Topological Sort:", topological_sort(dag))

    # Graph with a cycle for Topological Sort
    cyclic_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }

    print("Topological Sort (cyclic):", topological_sort(cyclic_graph))