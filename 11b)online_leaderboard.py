
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
            arr[largest_or_smallest], arr[i]
        )
        heapify(arr, n, largest_or_smallest, heap_type)


def heap_sort(arr, heap_type):
    n = len(arr)

    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, heap_type)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, heap_type)

    return arr


scores = list(map(int, input("Enter player scores: ").split()))

ascending = heap_sort(scores.copy(), "max")
descending = heap_sort(scores.copy(), "min")

print("\nLeaderboard - Ascending Order (Max Heap):")
print(ascending)

print("\nLeaderboard - Descending Order (Min Heap):")
print(descending)
