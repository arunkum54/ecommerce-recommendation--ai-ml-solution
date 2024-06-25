# ecommerce-recommendation--ai-ml-solution
# E-commerce AI/ML Solution

This project integrates AI models for automated content generation, personalized recommendations, and A/B testing for an e-commerce platform.
It includes mock API integrations to simulate interactions with external services like user data retrieval and product databases.


├── A/B Testing
│ ├── ab_test_framework.py
│ ├── analysis.py
├── Content_Desc_Generation
│ ├── content_desc.py
├── data
│ ├── ab_test_interactions.csv
│ ├── products_with_descriptions.csv
│ ├── products.csv
│ ├── user_interactions.csv
├── Dummy_data_Generation
│ ├── generate_dataset.py
│ ├── user_interaction.py
├── env
├── Mock_API
│ ├── content_generation_API.py
│ ├── mock_api.py
│ ├── recommendations_API.py
│ ├── Testing_API.py
│ ├── tests
│ │ ├── test_flask_apis.py
│ │ ├── test_recommendation_model.py
├── Recommendation_Model
│ ├── recommendation_model.h5
│ ├── recommendation_model.py
│ ├── most_purchased_clicked_viewed.csv
├── requirements.txt

#Prerequisites
Python 3.8 or higher
Virtual environment tools (venv or virtualenv)
Steps
Clone the repository:

#To clone

git clone https://github.com/arunkum54/ecommerce-recommendation--ai-ml-solution.git
cd ecommerce-recommendation--ai-ml-solution

#Install the required packages:
pip install -r requirements.txt

#API Endpoints

Fetch Product Attributes
Endpoint:
GET /api/products/<product_id>
Example:
GET http://127.0.0.1:5000/api/products/101

Fetch User Interactions
Endpoint:
GET /api/users/<user_id>/interactions
Example:
GET http://127.0.0.1:5000/api/users/1/interactions

Fetch Content Version
Endpoint:
GET /api/content/<version>
Example:
GET http://127.0.0.1:5000/api/content/A

Get Recommendations for a User
Endpoint:
GET /api/recommendations/<user_id>
Example:
GET http://127.0.0.1:5000/api/recommendations/1
