# Python program to recommend products based on user history
# Ethical Guidelines: This program is transparent about how recommendations are made and aims to treat all users fairly.

def collect_user_history():
    """
    Collects product history from the user.
    Returns a list of products the user has interacted with.
    """
    print("We collect your product history to recommend items you may like.")
    print("Please enter the names of products you have purchased or viewed, separated by commas.")
    history_input = input("Product history: ")
    user_history = [item.strip().lower() for item in history_input.split(",") if item.strip()]
    return user_history

def recommend_products(user_history, product_catalog):
    """
    Recommends products based on user history.
    The recommendation is based on simple matching of categories.
    """
    # Transparency: Recommendations are based on matching categories of products you've interacted with.
    # Fairness: All products in the catalog are considered equally, and no personal attributes are used.
    recommended = set()
    user_categories = set()
    for product in user_history:
        if product in product_catalog:
            user_categories.add(product_catalog[product]['category'])
    for product, info in product_catalog.items():
        if info['category'] in user_categories and product not in user_history:
            recommended.add(product)
    return list(recommended)

def main():
    # Example product catalog
    product_catalog = {
        'laptop': {'category': 'electronics'},
        'headphones': {'category': 'electronics'},
        'novel': {'category': 'books'},
        'cookbook': {'category': 'books'},
        't-shirt': {'category': 'clothing'},
        'jeans': {'category': 'clothing'},
        'smartphone': {'category': 'electronics'},
        'jacket': {'category': 'clothing'},
    }

    print("Welcome to the Product Recommender!")
    print("We value your privacy and fairness. Recommendations are made only from your provided product history and are not influenced by personal attributes.")
    user_history = collect_user_history()
    recommendations = recommend_products(user_history, product_catalog)

    print("\nBased on your history, we recommend the following products:")
    if recommendations:
        for product in recommendations:
            print("-", product.title())
    else:
        print("No recommendations available based on your history.")

    print("\nEthical Notice:")
    print("1. Your product history is used only for generating recommendations during this session.")
    print("2. No personal or sensitive data is collected or stored.")
    print("3. Recommendations are based solely on product categories, ensuring fairness and transparency.")

if __name__ == "__main__":
    main()
