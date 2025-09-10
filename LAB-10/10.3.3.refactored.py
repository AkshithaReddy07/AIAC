class Employee:
    def __init__(self, name, salary):  # Corrected constructor name
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

    def print_info(self):
        print(f"Employee: {self.name} Salary: {self.salary}")

# Example usage:
e = Employee("John", 5000)
e.print_info()      # Output: Employee: John Salary: 5000
e.increase_salary(10)
e.print_info()      # Output: Employee: John Salary: 5500.0