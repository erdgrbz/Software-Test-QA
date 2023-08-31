# HTTP response

import requests
import json

response = requests.get('https://flights-api.buraky.workers.dev/')

print(response)
# print(response.status_code)

if response.status_code != 200:
    print("Hata!")

print("\n")
#Response Contents

#print(response.content)
data = json.loads(response.content)

for flight in data["data"]:
    print("Flight {")
    print("    Id:", flight["id"])
    print("    From:", flight["from"])
    print("    To:", flight["to"])
    print("    Date:", flight["date"])
    print("},")

# Content Type
content_type = response.headers['Content-Type']

print("\n" ,content_type)

