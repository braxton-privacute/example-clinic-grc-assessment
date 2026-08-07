import requests

url = "https://grcengclub.github.io/scf-api/api/controls.json"

print("Fetching the SCF control list...")
response = requests.get(url)
print(f"Status code: {response.status_code}\n")

data = response.json()

print(f"Top-level type: {type(data)}")
print(f"Length: {len(data)}\n")

print("Top-Level keys:")
print(list(data.keys()))