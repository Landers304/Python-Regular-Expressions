#Task 1:


import re

def tag_product(description):
    keywords = {
        "Electronics": ["smartphone", "tablet", "laptop", "camera"],
        "Apparel": ["t-shirt", "shirt", "dress", "jeans"],
        "Home & Kitchen": ["knife", "kitchen", "cookware", "appliance"]
    }
    for tag, keyword_list in keywords.items():
        for keyword in keyword_list:
            if re.search(keyword, description, re.IGNORECASE):
                return tag
    return "Other"

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

# Tagged products based on keywords in the description
tagged_products = {description: tag_product(description) for description in descriptions}
print(tagged_products)
