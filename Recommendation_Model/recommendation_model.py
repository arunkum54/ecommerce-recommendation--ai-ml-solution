import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense

# Loading the datasets
product_df = pd.read_csv('data/products_with_descriptions.csv')
interaction_df = pd.read_csv('data/user_interactions.csv')

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

# Spliting data into training and test sets
train, test = train_test_split(interaction_df, test_size=0.2, random_state=42)

# Defining the recommendation model
num_users = len(user_ids)
num_products = len(product_ids)
embedding_size = 50

user_input = Input(shape=(1,), name='user_input')
product_input = Input(shape=(1,), name='product_input')

user_embedding = Embedding(input_dim=num_users, output_dim=embedding_size, name='user_embedding')(user_input)
product_embedding = Embedding(input_dim=num_products, output_dim=embedding_size, name='product_embedding')(product_input)

user_vector = Flatten()(user_embedding)
product_vector = Flatten()(product_embedding)

dot_product = Dot(axes=1)([user_vector, product_vector])
output = Dense(1, activation='linear')(dot_product)

model = Model(inputs=[user_input, product_input], outputs=output)
model.compile(optimizer='adam', loss='mean_squared_error')

# To Train the model
history = model.fit(
    [train['user_index'], train['product_index']],
    train['interaction_value'],
    epochs=10,
    verbose=1,
    validation_data=([test['user_index'], test['product_index']], test['interaction_value'])
)

# To save trained model
model.save('recommendation_model.h5')
print("Model saved as 'recommendation_model.h5'")

# To recommend products for a given user
def recommend_products(user_id, num_recommendations=10):
    user_index = user_id_to_index[user_id]
    product_indices = np.array(list(product_id_to_index.values()))
    user_indices = np.full_like(product_indices, user_index)

    predictions = model.predict([user_indices, product_indices])
    top_indices = predictions.flatten().argsort()[-num_recommendations:][::-1]
    top_product_ids = [product_ids[index] for index in top_indices]

    return product_df[product_df['product_id'].isin(top_product_ids)]

# Example to Get recommendations for user with ID 1
user_id = 1
recommended_products = recommend_products(user_id)
print(recommended_products)
