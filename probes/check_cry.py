import requests

for cid in ["CRY-01", "CRY-05", "CRY-06", "CRY-07", "CRY-08", "CRY-09"]:
    try:
        data = requests.get(f"https://grcengclub.github.io/scf-api/api/controls/{cid}.json").json()
        print(f"{cid}: {data['title']}")
    except Exception:
        print(f"{cid}: (not found)")