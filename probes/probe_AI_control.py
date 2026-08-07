import requests

data = requests.get("https://grcengclub.github.io/scf-api/api/controls.json").json()
controls = data["controls"]

# Find any control family related to AI / artificial intelligence / autonomous tech
print("Searching for AI-related controls...\n")
for c in controls:
    text = (c["control_id"] + " " + c["title"]).lower()
    if "artificial intelligence" in text or " ai " in text or text.startswith("aat") or "autonomous" in text or c["control_id"].startswith("AAT"):
        print(f"{c['control_id']}: {c['title']}")