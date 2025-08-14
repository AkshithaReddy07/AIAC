import csv

def read_student_marks(filename):
    students = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            try:
                marks = [float(row['Subject1']), float(row['Subject2']), float(row['Subject3'])]
            except ValueError:
                print(f"Invalid marks for student {name}. Skipping.")
                continue
            total = sum(marks)
            average = total / 3
            students.append({
                'Name': name,
                'Total': total,
                'Average': average
            })
    return students

def print_student_results(students):
    print("\nStudent Results:")
    for student in students:
        print(f"Name: {student['Name']}, Total: {student['Total']}, Average: {student['Average']:.2f}")

def main():
    filename = input("Enter the CSV filename (e.g., students.csv): ")
    try:
        students = read_student_marks(filename)
        print_student_results(students)
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
