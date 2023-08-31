# HTTP response

import requests

api_url = "https://flights-api.buraky.workers.dev/"
response = requests.get(api_url)

print(response)
# print(response.status_code)

if response.status_code == 200:
    print("GET Status Code: 200, Success.")
else:
    print("Request failed with status code:", response.status_code)

print("\n")


#Response Contents

data = response.json()
for flight in data["data"]:
    print("Flight {")
    print("    ID:", flight["id"])
    print("    From:", flight["from"])
    print("    To:", flight["to"])
    print("    Date:", flight["date"])
    print("}, ")

# Content Type

content_type = response.headers['Content-Type']
print("\n Content Type :" ,content_type)







