# Python script to collect user data

def collect_user_data():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['age'] = input("Enter your age: ")
    user_data['email'] = input("Enter your email: ")
    return user_data

def main():
    data = collect_user_data()
    print("Collected Data:", data)

    # --- Data Protection & Anonymization Comments ---
    # 1. Avoid storing raw personal data unless necessary.
    # 2. To anonymize, remove or hash identifiers (e.g., use hash(data['email'])).
    # 3. Store data in encrypted files or databases.
    # 4. Limit access to sensitive data.
    # 5. Regularly delete data that is no longer needed.
    # 6. Use pseudonyms or user IDs instead of real names/emails in logs or analytics.

if __name__ == "__main__":
    main()
