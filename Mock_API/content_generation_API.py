import requests

def fetch_product_attributes(product_id):
    url = f'http://127.0.0.1:5000/api/products/{product_id}'
    response = requests.get(url)
    if response.status_code == 200:
        product_data = response.json()
        return product_data
    else:
        print(f"Failed to fetch product {product_id}: {response.status_code}")
        return None

def generate_product_description(product_id):
    product = fetch_product_attributes(product_id)
    if product:
        description = f"This is {product['name']} by {product['brand']}. It is {product['color']} in color and size {product['size']}."
        return description
    else:
        return "No product description available."

if __name__ == "__main__":
    product_id = 101
    description = generate_product_description(product_id)
    print(description)
