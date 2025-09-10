def process_scores(scores):
    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

# Example usage:
process_scores([80, 95, 70, 100, 65])