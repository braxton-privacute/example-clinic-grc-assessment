import requests
import json

url = "https://grcengclub.github.io/scf-api/api/controls/CRY-03.json"
data = requests.get(url).json()
crosswalks = data["crosswalks"]

frameworks_of_interest = [
    "usa-federal-law-hipaa-security-rule-2013",
    "general-nist-csf-2-0",
]

print("Crosswalk shapes for CRY-03 (Transmission Confidentiality):\n")
for fw in frameworks_of_interest:
    value = crosswalks.get(fw, "NOT MAPPED")
    print(f"{fw}")
    print(f"   type: {type(value).__name__}")
    print(f"   value: {value}\n")