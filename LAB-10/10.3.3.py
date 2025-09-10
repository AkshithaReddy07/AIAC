class emp:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    def inc(self, p):
        self.s = self.s + (self.s * p / 100)
    def pr(self):
        print("emp:", self.n, "salary:", self.s)

# Example usage:
e = emp("John", 5000)
e.pr()         # Output: emp: John salary: 5000
e.inc(10)      # Increase salary by 10%
e.pr()         # Output: emp: John salary: 5500.0