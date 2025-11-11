'''
Case Study: E-Commerce Product Management System
Description:
An online store wants to manage its products efficiently. Each product has:
Product ID (unique)
Name
Category
Price
Tags (like “Electronics”, “Portable”, “NewArrival”)
Ratings (multiple customer ratings)
Sample Input
List of Products (Sequential Access)
products = [
    {"id": 101, "name": "Laptop", "category": "Electronics", "price": 70000, "tags": {"Electronics", "Portable"}, "ratings": (5, 4, 5)},
    {"id": 102, "name": "Smartphone", "category": "Electronics", "price": 40000, "tags": {"Electronics", "Mobile", "Portable"}, "ratings": (4, 5, 4, 5)},
    {"id": 103, "name": "Office Chair", "category": "Furniture", "price": 8000, "tags": {"Furniture", "Office"}, "ratings": (4, 4, 3)},
]
Operations to Perform
Add a new product:
ID: 104, Name: "Headphones", Category: "Electronics", Price: 3500, Tags: {"Electronics", "Audio"}, Ratings: (5, 4)
Update price of product 102 to 42000.
Add a new tag "Discount" to product 101.
Calculate average rating for each product.
List all unique tags across all products.
List all product categories (without duplicates).
'''

products = [
    {"id": 101, "name": "Laptop", "category": "Electronics",'price': 70000, "tags": {"Electronics", "Portable"}, "ratings": (5, 4, 5)},
    {"id": 102, "name": "Smartphone", "category": "Electronics", 'price': 40000, "tags": {"Electronics", "Mobile", "Portable"}, "ratings": (4, 5, 4, 5)},
    {"id": 103, "name": "Office Chair", "category": "Furniture", 'price': 8000, "tags": {"Furniture", "Office"}, "ratings": (4, 4, 3)},
]


# Add a new product
new_product = {
    "id": 104,
    "name": "Headphones",
    "category": "Electronics",
    "price": 3500,
    "tags": {"Electronics", "Audio"},
    "ratings": (5, 4)
}
products.append(new_product)
print("After adding new product:", products, "\n")

# Update price of product 102 to 42000
for product in products:
    if product["id"] == 102:
        product["price"] = 42000
        break
print("After updating price of product 102:", products, "\n")

# Add a new tag "Discount" to product 101
for product in products:
    if product["id"] == 101:
        product["tags"].add("Discount")
        break
print("After adding new tag to product 101:", products, "\n")

# Calculate average rating for each product
for product in products:
    total_ratings = sum(product["ratings"])
    num_ratings = len(product["ratings"])
    average_rating = total_ratings / num_ratings
    product["average_rating"] = average_rating
print("After calculating average rating for each product:", products, "\n")

# List all unique tags across all products
all_unique_tags = set()
for product in products:
    all_unique_tags = all_unique_tags.union(product["tags"])
print("All unique tags across all products:", all_unique_tags, "\n")

# List all product categories (without duplicates)
all_categories = set()
for product in products:
    all_categories.add(product["category"])
print("All product categories (without duplicates):", all_categories, "\n")