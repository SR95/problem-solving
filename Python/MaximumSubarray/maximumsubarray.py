def maxSubArray(numbers):
    """Find a contiguous subarray with the largest sum."""
    best_sum = 0 if (0<numbers[0]) else numbers[0]
    current_sum = 0 if (0<numbers[0]) else numbers[0]
    for x in numbers:
        current_sum = x if (x > (current_sum + x)) else (current_sum + x)
        best_sum = best_sum if (best_sum > current_sum) else current_sum
    return best_sum