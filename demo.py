def count_frequency(str: str):
    freq = {}
    for char in str:
        freq[char] = freq.get(char, 0) + 1
    # return freq  # count frequency
    max_freq = max(freq, key = freq.get)
    return max_freq     # To find max frequency

print(count_frequency('balloon'))
