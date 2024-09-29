import random

# Deterministic Algorithm (Median of Medians)

def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Split arr into sublists of 5 elements
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    median_of_medians_value = median_of_medians(medians, len(medians)//2)

    # Partition around the median of medians
    low = [x for x in arr if x < median_of_medians_value]
    high = [x for x in arr if x > median_of_medians_value]

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(arr) - len(high):
        return median_of_medians_value
    else:
        return median_of_medians(high, k - (len(arr) - len(high)))

# Randomized Algorithm (Randomized Quickselect)

def randomized_partition(arr, left, right):
    pivot_idx = random.randint(left, right)
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def randomized_select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_idx = randomized_partition(arr, left, right)
    if k == pivot_idx:
        return arr[pivot_idx]
    elif k < pivot_idx:
        return randomized_select(arr, left, pivot_idx - 1, k)
    else:
        return randomized_select(arr, pivot_idx + 1, right, k)
