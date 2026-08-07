import requests

data = requests.get("https://grcengclub.github.io/scf-api/api/controls/CRY-05.json").json()
cw = data.get("crosswalks", {})

print("CRY-05:", data["title"])
print()

# Show any HIPAA-related crosswalk keys on CRY-05
hipaa_keys = [k for k in cw if "hipaa" in k.lower()]
print("HIPAA crosswalk keys on CRY-05:", hipaa_keys)
for k in hipaa_keys:
    print(f"  {k}: {cw[k]}")

print()
print("NIST CSF 2.0:", cw.get("general-nist-csf-2-0", "NOT MAPPED"))