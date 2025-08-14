import re

def extract_emails(text):
    # Regular expression for matching email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

if __name__ == "__main__":
    user_input = input("Enter the text to extract emails from:\n")
    emails = extract_emails(user_input)
    print("Extracted emails:", emails)