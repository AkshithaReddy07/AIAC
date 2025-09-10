from collections import Counter

def find_common(a, b):
    ca, cb = Counter(a), Counter(b)
    res = []
    for elem in ca:
        if elem in cb:
            res.extend([elem] * min(ca[elem], cb[elem]))
    return res

# Example usage:
print(find_common([1, 2, 3, 4], [3, 4, 4, 5, 6]))  # Output: [3, 4, 4]