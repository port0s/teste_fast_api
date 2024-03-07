import httpx

response = httpx.get('http://127.0.0.1:8000/example')
print(f'{response}')

content = response.text
print(f'{content}')


data = {'inp': 123, 'inp2': 'Olá, post!'}
post = httpx.post('http://127.0.0.1:8000/example_2', json=data)
print(f"{post.text}")
