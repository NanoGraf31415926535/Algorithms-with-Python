def linear_search(data, target):
    """Performs a linear search for the target element in the data."""
    for i in range(len(data)):
        if data[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

def binary_search(data, target):
    """Performs a binary search for the target element in the sorted data."""
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def depth_first_search(graph, start_node, target):
    """Performs a depth-first search to find the target in a graph."""
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node == target:
            return True
        if node not in visited:
            visited.add(node)
            # Add neighbors in reverse order to explore in a typical DFS manner
            neighbors = list(graph.get(node, []))
            neighbors.reverse()
            stack.extend(neighbors)
    return False

def breadth_first_search(graph, start_node, target):
    """Performs a breadth-first search to find the target in a graph."""
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    while queue:
        node = queue.pop(0)
        if node == target:
            return True
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def jump_search(data, target):
    """Performs a jump search for the target element in the sorted data."""
    n = len(data)
    step = int(n**0.5)  # Optimal step size is often sqrt(n)
    left = 0
    right = step
    while left < n and data[left] <= target:
        if data[left] == target:
            return left
        left = right
        right += step
        if right > n:
            right = n
    # Perform linear search in the block
    for i in range(left, right):
        if data[i] == target:
            return i
    return -1

def interpolation_search(data, target):
    """Performs an interpolation search for the target in sorted data."""
    low = 0
    high = len(data) - 1
    while low <= high and data[low] <= target <= data[high]:
        if low == high:
            if data[low] == target:
                return low
            return -1

        # Interpolation formula
        pos = low + ((target - data[low]) * (high - low)) // (data[high] - data[low])

        if data[pos] == target:
            return pos
        elif data[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# For hash table search, we can directly use Python's dictionary (dict)
# which provides efficient average-case O(1) lookups.

# Example Usage:
if __name__ == "__main__":
    linear_data = [5, 2, 8, 1, 9, 4]
    print("Linear Search:", linear_search(linear_data, 4))  # Output: 5
    print("Linear Search (not found):", linear_search(linear_data, 10)) # Output: -1

    binary_data = sorted(linear_data)
    print("Binary Search (sorted data):", binary_search(binary_data, 4)) # Output: 2
    print("Binary Search (not found):", binary_search(binary_data, 10)) # Output: -1

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("DFS (graph):", depth_first_search(graph, 'A', 'F')) # Output: True
    print("DFS (not found):", depth_first_search(graph, 'A', 'G')) # Output: False

    print("BFS (graph):", breadth_first_search(graph, 'A', 'F')) # Output: True
    print("BFS (not found):", breadth_first_search(graph, 'A', 'G')) # Output: False

    jump_data = sorted(linear_data)
    print("Jump Search (sorted data):", jump_search(jump_data, 4)) # Output: 2
    print("Jump Search (not found):", jump_search(jump_data, 10)) # Output: -1

    interpolation_data = sorted(linear_data)
    print("Interpolation Search (sorted data):", interpolation_search(interpolation_data, 4)) # Output: 2
    print("Interpolation Search (not found):", interpolation_search(interpolation_data, 10)) # Output: -1

    hash_table = {'apple': 1, 'banana': 2, 'cherry': 3}
    print("Hash Table Search:", 'banana' in hash_table) # Output: True
    print("Hash Table Search (value):", hash_table.get('banana')) # Output: 2
    print("Hash Table Search (not found):", 'grape' in hash_table) # Output: False