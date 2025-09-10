def find_common(a, b):
    res = []
    for i in a:
        for j in b:
            if i == j:
                res.append(i)
    return res

# Example usage:
print(find_common([1, 2, 3, 4], [3, 4, 4, 5, 6]))  # Output: [3, 4, 4]