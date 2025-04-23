def merge_sort_dc(data):
    """Sorts a list using the Merge Sort algorithm (Divide and Conquer)."""
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort_dc(left)
    right_sorted = merge_sort_dc(right)

    return _merge_dc(left_sorted, right_sorted)

def _merge_dc(left, right):
    """Helper function to merge two sorted lists for Merge Sort."""
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

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def quick_sort_dc(data):
    """Sorts a list using the Quick Sort algorithm (Divide and Conquer)"""
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort_dc(left) + middle + quick_sort_dc(right)

def binary_search_dc(data, target):
    """Performs Binary Search on a sorted list (Divide and Conquer)."""
    return _binary_search_recursive_dc(data, target, 0, len(data) - 1)

def _binary_search_recursive_dc(data, target, low, high):
    """Recursive helper function for Binary Search."""
    if low > high:
        return -1
    mid = (low + high) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return _binary_search_recursive_dc(data, target, mid + 1, high)
    else:
        return _binary_search_recursive_dc(data, target, low, mid - 1)

# Example Usage:
if __name__ == "__main__":
    unsorted_list_dc = [5, 1, 4, 2, 8, -2, 0, 9, 3]
    print("Original list:", unsorted_list_dc)

    merge_sorted_dc = merge_sort_dc(unsorted_list_dc.copy())
    print("Merge Sort (DC):", merge_sorted_dc)

    quick_sorted_dc = quick_sort_dc(unsorted_list_dc.copy())
    print("Quick Sort (DC):", quick_sorted_dc)

    sorted_list_bs_dc = sorted(unsorted_list_dc)
    target_bs_dc = 4
    index_bs_dc = binary_search_dc(sorted_list_bs_dc, target_bs_dc)
    print(f"Binary Search (DC) for {target_bs_dc} in {sorted_list_bs_dc}: Index {index_bs_dc}")

    target_bs_dc_not_found = 10
    index_bs_dc_nf = binary_search_dc(sorted_list_bs_dc, target_bs_dc_not_found)
    print(f"Binary Search (DC) for {target_bs_dc_not_found} in {sorted_list_bs_dc}: Index {index_bs_dc_nf}")