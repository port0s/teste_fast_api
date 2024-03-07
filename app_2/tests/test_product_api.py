import httpx

def test_should_get_list_of_products():
    response = httpx.get('http://127.0.0.1:8000/products')
    print(f'{response.json()}')

test_should_get_list_of_products()
