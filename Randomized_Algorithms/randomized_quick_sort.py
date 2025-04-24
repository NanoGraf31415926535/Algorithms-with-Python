import random

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [i for i in arr[:pivot_index] + arr[pivot_index+1:] if i <= pivot]
    greater = [i for i in arr[:pivot_index] + arr[pivot_index+1:] if i > pivot]
    return randomized_quick_sort(less) + [pivot] + randomized_quick_sort(greater)

# Example Usage
if __name__ == "__main__":
    my_array = [5, 2, 8, 1, 9, 4, 7, 3, 6]
    sorted_array = randomized_quick_sort(my_array)
    print("Original array:", my_array)
    print("Sorted array:", sorted_array)