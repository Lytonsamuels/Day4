def recur_sum(numbers):

    total = 0

    for index in numbers:
        if isinstance(index, list):
            total += recur_sum(index)

        elif isinstance(index, int):
            total += index
    return total