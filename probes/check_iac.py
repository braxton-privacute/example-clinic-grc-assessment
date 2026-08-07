import requests

for cid in ["IAC-06", "IAC-01", "IAC-02"]:
    data = requests.get(f"https://grcengclub.github.io/scf-api/api/controls/{cid}.json").json()
    cw = data.get("crosswalks", {})
    hipaa = cw.get("usa-federal-law-hipaa-security-rule-2013", [])
    csf = cw.get("general-nist-csf-2-0", [])
    print(f"{cid}: {data['title']}")
    print(f"   HIPAA: {hipaa}")
    print(f"   NIST CSF: {csf}\n")