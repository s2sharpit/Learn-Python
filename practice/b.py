from heapq import heappush, heappop


def lexicographically_smallest_string(S):
    ray = list(S)
    ben = []
    kevin = []

    while ray or ben:
        # Move characters from Ray to Ben as long as Ray is not empty
        while ray:
            heappush(ben, ray.pop(0))

        # Move the smallest character from Ben to Kevin
        while ben:
            kevin.append(heappop(ben))

    return "".join(kevin)


# Example usage:
S = "bca"
print(lexicographically_smallest_string(S))  # Output: "abc"
