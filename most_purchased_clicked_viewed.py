import pandas as pd

# Loading the datasets
products_df = pd.read_csv('products_with_descriptions.csv')
user_interactions_df = pd.read_csv('user_interactions.csv')

# Merged the datasets on 'product_id'
merged_df = pd.merge(user_interactions_df, products_df, on='product_id', how='left')

interaction_counts = merged_df.groupby(['product_id', 'name', 'interaction']).size().unstack(fill_value=0)

# Calculating total interactions per product
interaction_counts['total_interactions'] = interaction_counts.sum(axis=1)

# Sorting products by total interactions
sorted_interactions = interaction_counts.sort_values(by='total_interactions', ascending=False)

# Saved interaction analysis to a CSV file
sorted_interactions.to_csv('product_interactions_analysis.csv')

# Display the top 10 most interacted products
print("Top 10 most interacted products:")
print(sorted_interactions.head(10))

# Most viewed products
most_viewed = sorted_interactions.sort_values(by='view', ascending=False).head(10)
print("\nTop 10 most viewed products:")
print(most_viewed[['view']])

# Most clicked products
most_clicked = sorted_interactions.sort_values(by='click', ascending=False).head(10)
print("\nTop 10 most clicked products:")
print(most_clicked[['click']])

# Most purchased products
most_purchased = sorted_interactions.sort_values(by='purchase', ascending=False).head(10)
print("\nTop 10 most purchased products:")
print(most_purchased[['purchase']])
