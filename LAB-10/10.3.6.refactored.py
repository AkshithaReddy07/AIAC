def grade(score):
    grades = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
    for threshold, letter in grades:
        if score >= threshold:
            return letter
    return "F"

# Example usage:
print(grade(95))  # Output: A
print(grade(82))  # Output: B
print(grade(75))  # Output: C
print(grade(65))  # Output: D
print(grade(50))  # Output: F