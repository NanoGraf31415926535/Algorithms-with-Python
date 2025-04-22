def bubble_sort(data):
    """Sorts a list using the Bubble Sort algorithm."""
    n = len(data)
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                # Swap if the element found is greater than the next element
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def insertion_sort(data):
    """Sorts a list using the Insertion Sort algorithm."""
    for i in range(1, len(data)):
        key = data[i]
        # Move elements of data[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def merge_sort(data):
    """Sorts a list using the Merge Sort algorithm."""
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return _merge(left_sorted, right_sorted)

def _merge(left, right):
    """Helper function to merge two sorted lists."""
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from left or right sublists
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def quick_sort(data):
    """Sorts a list using the Quick Sort algorithm."""
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(data):
    """Sorts a list using the Heap Sort algorithm."""
    import heapq
    heapq.heapify(data)  # Transform list into a min-heap
    sorted_data = [heapq.heappop(data) for _ in range(len(data))]
    return sorted_data

# Example usage:
if __name__ == "__main__":
    unsorted_list = [5, 1, 4, 2, 8, -2, 0, 9, 3]

    print("Original list:", unsorted_list)

    bubble_sorted = bubble_sort(unsorted_list.copy())
    print("Bubble Sort:", bubble_sorted)

    insertion_sorted = insertion_sort(unsorted_list.copy())
    print("Insertion Sort:", insertion_sorted)

    merge_sorted = merge_sort(unsorted_list.copy())
    print("Merge Sort:", merge_sorted)

    quick_sorted = quick_sort(unsorted_list.copy())
    print("Quick Sort:", quick_sorted)

    heap_sorted = heap_sort(unsorted_list.copy())
    print("Heap Sort:", heap_sorted)