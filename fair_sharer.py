def fair_sharer(values, num_iterations, share=0.1):
    """Distributes a fraction of the highest value to its neighbors."""
    from copy import deepcopy
    values = deepcopy(values)  # Prevent modifying the input list directly

    for _ in range(num_iterations):
        # Find the index of the highest value in the list
        max_index = values.index(max(values))

        # Compute the indices of the left and right neighbors (with wrapping)
        left_index = (max_index - 1) % len(values)
        right_index = (max_index + 1) % len(values)

        # Calculate how much to distribute
        distributed_amount = values[max_index] * share

        # Update the values of the current element and its neighbors
        values[max_index] -= 2 * distributed_amount
        values[left_index] += distributed_amount
        values[right_index] += distributed_amount

    return values
