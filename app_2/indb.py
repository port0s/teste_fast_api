from product import Product
import json

def generate_products():
    list_products = []

    for x in range(10):
    p = Product(name = f"Product {x + 1}", price = 4.90 * x)
    list_products.append(p)

    return list_products

def open_file_load_json():
    f = open('./data/products.json')
    data = json.loads(f.read())
    f.close()
    return data
