import requests

response = requests.get('https://flights-api.buraky.workers.dev/')

content_type = response.headers['Content-Type']

print(content_type)