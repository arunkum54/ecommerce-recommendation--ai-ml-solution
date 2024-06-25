import pandas as pd
import numpy as np

def generate_product_data(num_products):
    product_ids = np.arange(101, 101 + num_products)
    names = [f"Product {i}" for i in range(1, num_products + 1)]
    brands = [f"Brand {i % 5}" for i in range(num_products)]
    colors = ["Red", "Black", "Blue", "Silver", "Gray", "Green", "Orange"]
    sizes = ["10", "N/A", "M", "N/A", "15-inch", "N/A", "L"]
    materials = ["Synthetic", "Plastic", "Cotton", "Metal", "Aluminum", "Paper", "Wool", "Leather"]

    data = {
        "product_id": product_ids,
        "name": names,
        "brand": [brands[i % len(brands)] for i in range(num_products)],
        "color": [colors[i % len(colors)] for i in range(num_products)],
        "size": [sizes[i % len(sizes)] for i in range(num_products)],
        "material": [materials[i % len(materials)] for i in range(num_products)]
    }

    return pd.DataFrame(data)

def generate_user_interaction_data(num_users, num_interactions, num_products):
    user_ids = np.random.randint(1, num_users + 1, size=num_interactions)
    product_ids = np.random.choice(np.arange(101, 101 + num_products), size=num_interactions)
    interactions = np.random.choice(["view", "click", "purchase"], size=num_interactions)

    data = {
        "user_id": user_ids,
        "product_id": product_ids,
        "interaction": interactions
    }

    return pd.DataFrame(data)

# Parameters
num_products = 200
num_users = 50
num_interactions = 1000

# Generating datasets
product_df = generate_product_data(num_products)
user_interaction_df = generate_user_interaction_data(num_users, num_interactions, num_products)


product_df.to_csv('data/products.csv', index=False)
user_interaction_df.to_csv('data/user_interactions.csv', index=False)
print("Product attributes dataset created as 'products.csv'")
print("User interactions dataset created as 'user_interactions.csv'")
