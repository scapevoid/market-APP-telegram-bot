import json

def get_products(index):
    
    # Return the product list
    try:
        with open(f"backend/data/productlist{index}.json", 'r') as file:
            lines = file.readlines()
            if not lines:
                print(f"Error: File 'backend/data/productlist{index}.json' is empty.")
                products = {"none": "File is empty"}
            else:
                content = ''.join(lines).strip()
                products = json.loads(content)
                print(products)
    except FileNotFoundError:
        print(f"Error: File 'backend/data/productlist{index}.json' not found.")
        products = {"none": "File not found"}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from 'backend/data/productlist{index}.json'.")
        products = {"none": "Error decoding JSON"}
    return products