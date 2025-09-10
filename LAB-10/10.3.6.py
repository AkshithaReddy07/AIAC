def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example usage:
print(grade(95))  # Output: A
print(grade(82))  # Output: B
print(grade(75))  # Output: C
print(grade(65))  # Output: D
print(grade(50))  # Output: F