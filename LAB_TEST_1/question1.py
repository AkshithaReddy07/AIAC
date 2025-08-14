exchange_rates = {
    'USD': 1.0,
    'EUR': 0.92,
    'GBP': 0.79,
    'JPY': 145.0
}

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Currency not supported.")
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    return round(converted, 4)

if __name__ == "__main__":
    print("Available currencies:", ', '.join(exchange_rates.keys()))
    amount = float(input("Enter amount: "))
    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()
    try:
        result = convert_currency(amount, from_currency, to_currency, exchange_rates)
        print(f"{amount} {from_currency} = {result} {to_currency}")
    except Exception as e:
        print("Error:", e)