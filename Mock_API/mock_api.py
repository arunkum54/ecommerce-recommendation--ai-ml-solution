from flask import Flask, jsonify, request
import pandas as pd
import tensorflow as tf
import numpy as np

# Loading your product data
product_df = pd.read_csv('data/products.csv')

# Loading user interaction data (for simulation)
interaction_df = pd.read_csv('data/user_interactions.csv')
# Loading the recommendation model
model = tf.keras.models.load_model('Recommendation_Model/recommendation_model.h5')

app = Flask(__name__)

# Routing to fetch product attributes by product_id
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_df.loc[product_df['product_id'] == product_id].to_dict('records')
    if len(product) == 0:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product[0])

# Routing to fetch user interactions by user_id (for simulation)
@app.route('/api/users/<int:user_id>/interactions', methods=['GET'])
def get_user_interactions(user_id):
    user_interactions_data = interaction_df[interaction_df['user_id'] == user_id].to_dict('records')
    if len(user_interactions_data) == 0:
        return jsonify({'error': 'User interactions not found'}), 404
    return jsonify({'user_id': user_id, 'interactions': user_interactions_data})

# Preparing data for the recommendation system
user_ids = interaction_df['user_id'].unique()
product_ids = interaction_df['product_id'].unique()

# Mapping user ids and product ids to indices
user_id_to_index = {user_id: index for index, user_id in enumerate(user_ids)}
product_id_to_index = {product_id: index for index, product_id in enumerate(product_ids)}

interaction_df['user_index'] = interaction_df['user_id'].map(user_id_to_index)
interaction_df['product_index'] = interaction_df['product_id'].map(product_id_to_index)

# Converting interaction type to numerical values
interaction_mapping = {'view': 1, 'click': 2, 'purchase': 3}
interaction_df['interaction_value'] = interaction_df['interaction'].map(interaction_mapping)

# Spliting data into training and test sets (if needed for real-time recommendations)
train, test = interaction_df, None 



# To recommend products for a given user
def recommend_products(user_id, num_recommendations=10):
    user_index = user_id_to_index[user_id]
    product_indices = np.array(list(product_id_to_index.values()))
    user_indices = np.full_like(product_indices, user_index)

    predictions = model.predict([user_indices, product_indices])
    top_indices = predictions.flatten().argsort()[-num_recommendations:][::-1]
    top_product_ids = [product_ids[index] for index in top_indices]

    return product_df[product_df['product_id'].isin(top_product_ids)]

# Routing to get recommendations for a specific user
@app.route('/api/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    recommended_products = recommend_products(user_id)
    if recommended_products.empty:
        return jsonify({'error': 'No recommendations found for the user'}), 404
    else:
        recommendations = recommended_products.to_dict(orient='records')
        return jsonify({'user_id': user_id, 'recommendations': recommendations})


# Content for different versions
content_versions = {
    'A': 'This is content version A.',
    'B': 'This is content version B.',
    'C': 'This is content version C.'
}

# Routing to fetch content by version
@app.route('/api/content/<version>', methods=['GET'])
def get_content(version):
    if version in content_versions:
        return jsonify({'version': version, 'content': content_versions[version]})
    else:
        return jsonify({'error': 'Content version not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
