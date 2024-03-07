from fastapi import FastAPI
from product import Product
# from indb import generate_products
from json_db import JsonDB

app = FastAPI()

# products = generate_products()
productDB = JsonDB(path='./data/products.json')

@app.get('/products')
def get_products():
    products = productDB.read()
    return {"products": products}


@app.post('/products')
def create_product(Product: Product):

    productDB.insert(Product)

    return {"status": "insert"}
