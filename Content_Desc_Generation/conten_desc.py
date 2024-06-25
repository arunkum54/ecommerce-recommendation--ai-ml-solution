import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline

# Loading product data
product_df = pd.read_csv('data/products.csv')

# Loading pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer, truncation=True)

def generate_product_descriptions(product_df):
    descriptions = []

    for index, row in product_df.iterrows():
        product_name = row['name']
        product_brand = row['brand']
        product_color = row['color']
        product_size = row['size']
        product_material = row['material']

        # Constructing a prompt for the model
        prompt = f"Generate a product description for a {product_color} {product_size} {product_material} {product_brand} {product_name}."

        try:
            # Generating text using the model
            generated_text = text_generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
            descriptions.append(generated_text.strip())
        except Exception as e:
            print(f"Error generating description for product {product_name}: {str(e)}")
            descriptions.append(None)

    return descriptions

# Generating descriptions
product_df['description'] = generate_product_descriptions(product_df)

# To Display or save the updated product data with descriptions
print(product_df[['product_id', 'name', 'description']].head())

# To Save with descriptions
product_df.to_csv('products_with_descriptions.csv', index=False)
print("Product data with descriptions saved as 'products_with_descriptions.csv'")
