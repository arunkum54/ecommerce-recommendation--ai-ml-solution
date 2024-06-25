import pandas as pd
import numpy as np

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

# Number of Parameters
num_users = 50  
num_interactions = 1000 
num_products = 200  

# Generating user interactions dataset
user_interaction_df = generate_user_interaction_data(num_users, num_interactions, num_products)

user_interaction_df.to_csv('data/user_interactions.csv', index=False)
print("User interactions dataset created as 'user_interactions.csv'")
