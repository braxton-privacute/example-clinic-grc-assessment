import requests

data = requests.get("https://grcengclub.github.io/scf-api/api/controls.json").json()
controls = data["controls"]

# Show the DCH family top-level controls
print("Data handling / governance controls:\n")
for c in controls:
    cid = c["control_id"]
    if cid.startswith("DCH-") and cid.count(".") == 0:
        print(f"{cid}: {c['title']}")