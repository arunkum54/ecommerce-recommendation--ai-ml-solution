import requests

def fetch_user_interactions(user_id):
    url = f'http://127.0.0.1:5000/api/users/{user_id}/interactions'
    response = requests.get(url)
    if response.status_code == 200:
        interactions = response.json()
        return interactions
    else:
        print(f"Failed to fetch interactions for user {user_id}: {response.status_code}")
        return []

def get_user_preferences(user_id):
    interactions = fetch_user_interactions(user_id)
    preferences = {}
    for interaction in interactions:
        if interaction['interaction'] == 'purchase':
            product_id = interaction['product_id']
            if product_id in preferences:
                preferences[product_id] += 1
            else:
                preferences[product_id] = 1
    return preferences

if __name__ == "__main__":
    user_id = 1
    preferences = get_user_preferences(user_id)
    print(f"User {user_id} preferences: {preferences}")
