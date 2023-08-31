# requests bir HTTP kütüphanesidir.
import requests

response = requests.get('https://flights-api.buraky.workers.dev/')

print(response)

# print(response.status_code)