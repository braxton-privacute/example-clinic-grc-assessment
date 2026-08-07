import requests

data = requests.get("https://grcengclub.github.io/scf-api/api/controls.json").json()
controls = data["controls"]

print("Third-party management controls:\n")
for c in controls:
    cid = c["control_id"]
    if cid.startswith("TPM-") and cid.count(".") == 0:
        print(f"{cid}: {c['title']}")