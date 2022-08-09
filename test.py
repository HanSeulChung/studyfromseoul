import requests
data = requests.get("https://serverless-api.bell23bella.workers.dev/").json()
id = data["results"][0]["properties"]["이름"]["id"].plain_text
print(data)
print(id)