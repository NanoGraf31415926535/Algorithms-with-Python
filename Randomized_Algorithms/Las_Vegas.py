import random

def randomized_select(arr, k):
    if not arr:
        return None
    if k < 1 or k > len(arr):
        raise ValueError("k is out of bounds")

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]

    if k <= len(less):
        return randomized_select(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        return randomized_select(greater, k - len(less) - len(equal))

# Example Usage
if __name__ == "__main__":
    my_array = [5, 2, 8, 1, 9, 4, 7, 3, 6]
    k = 5  # Find the 5th smallest element
    kth_smallest = randomized_select(my_array, k)
    print(f"The {k}th smallest element in {my_array} is: {kth_smallest}")
    print(f"Sorted array: {sorted(my_array)}")