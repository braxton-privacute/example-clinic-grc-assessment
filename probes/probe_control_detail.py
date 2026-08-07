import requests
import json

# Fetch the FULL detail for one control we care about
url = "https://grcengclub.github.io/scf-api/api/controls/CRY-03.json"

print("Fetching full detail for CRY-03...")
response = requests.get(url)
print(f"Status code: {response.status_code}\n")

data = response.json()

# Show every top-level field name so we can find where HIPAA lives
print("Top-level keys in this control:")

crosswalks = data["crosswalks"]

crosswalks = data["crosswalks"]

hipaa_key = "usa-federal-law-hipaa-security-rule-2013"
hipaa = crosswalks[hipaa_key]

print(f"HIPAA Security Rule mapping for CRY-03:")
print(f"   type: {type(hipaa)}")
print(f"   value: {hipaa}")