import pandas as pd
import numpy as np

# Simulating interactions for A/B testing
def simulate_interactions(num_users, num_interactions):
    user_ids = np.random.randint(1, num_users + 1, size=num_interactions)
    product_ids = np.random.randint(101, 301, size=num_interactions) 
    interactions = np.random.choice(["view", "click", "purchase"], size=num_interactions)
    groups = np.random.choice(['A', 'B'], size=num_interactions) 

    data = {
        "user_id": user_ids,
        "product_id": product_ids,
        "interaction": interactions,
        "group": groups 
    }

    interactions_df = pd.DataFrame(data)
    interactions_df.to_csv('data/ab_test_interactions.csv', index=False)
    print(f"Logged {num_interactions} interactions for {num_users} users.")

if __name__ == "__main__":
    num_users = 1000
    num_interactions = 5000

    simulate_interactions(num_users, num_interactions)
