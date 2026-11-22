
# Assignment 11A: Heap Sort
# Min Heap - Descending Order
# Max Heap - Ascending Order

# Heapify Function
def heapify(arr, n, i, heap_type):
    largest_or_smallest = i

    left = 2 * i + 1
    right = 2 * i + 2

    if heap_type == "max":
        if left < n and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left

        if right < n and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right

    else:
        if left < n and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left

        if right < n and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right

    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = (
            arr[largest_or_smallest],
            arr[i]
        )

        heapify(arr, n, largest_or_smallest, heap_type)


# Heap Sort Function
def heap_sort(arr, heap_type):
    n = len(arr)

    # Build Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, heap_type)

    # Extract Elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0, heap_type)

    return arr


# Main Program
numbers = list(map(
    int, input("Enter numbers separated by spaces: ").split()
))

print("\nOriginal Array:", numbers)

# Max Heap - Ascending Order
max_heap_arr = numbers.copy()
heap_sort(max_heap_arr, "max")

print("\nMax Heap - Ascending Order:")
print(max_heap_arr)

# Min Heap - Descending Order
min_heap_arr = numbers.copy()
heap_sort(min_heap_arr, "min")

print("\nMin Heap - Descending Order:")
print(min_heap_arr)
