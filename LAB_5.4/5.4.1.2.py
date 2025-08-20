# Python script to collect user data with email masking for privacy

def mask_email(email):
    """
    Masks the email address for privacy.
    Example: john.doe@gmail.com -> j*****@gmail.com
    """
    try:
        local, domain = email.split('@')
        if len(local) > 1:
            masked_local = local[0] + '*' * (len(local) - 1)
        else:
            masked_local = '*'
        return masked_local + '@' + domain
    except Exception:
        # If email format is invalid, return as is
        return email

def collect_user_data():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['age'] = input("Enter your age: ")
    email = input("Enter your email: ")
    user_data['email'] = mask_email(email)  # Store masked email for protection
    return user_data

def main():
    data = collect_user_data()
    print("Collected Data (with protected email):", data)

    # --- Data Protection & Anonymization Comments ---
    # 1. Avoid storing raw personal data unless absolutely necessary.
    # 2. Mask or anonymize sensitive fields (e.g., use mask_email for emails).
    # 3. To further anonymize, remove or hash identifiers (e.g., hash(data['email'])).
    # 4. For strong protection, encrypt sensitive data before storage.
    # 5. Limit access to personal data and regularly delete unnecessary records.
    # 6. Use pseudonyms or user IDs instead of real names/emails in logs or analytics.

if __name__ == "__main__":
    main()
