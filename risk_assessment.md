# Risk Assessment

Findings mapped to the Secure Controls Framework (SCF), scored on a 5x5 likelihood x impact matrix. HIPAA references are from the SCF crosswalk unless marked otherwise.

| ID | Threat | SCF Controls | L | I | Score | Band | Status | HIPAA Refs | Remediation |
|----|--------|--------------|---|---|-------|------|--------|------------|-------------|
| EFC-001 | Exfiltration of ePHI via vendor database | TPM-02, TPM-05 | 5 | 5 | 25 | Critical | Open | 164.308(a)(7)(ii)(E), 164.308(b)(1), 164.308(b)(2), 164.308(b)(3), 164.314(a)(2)(iii), 164.314(b)(1), 164.314(b)(2)(i), 164.314(b)(2)(ii), 164.314(b)(2)(iii) | Vendor freeze; collect SOC 2; execute BAA before data flow resumes |
| EFC-002 | Unverified e-Rx data flow between EHR and pharmacy | AST-02.8, CRY-03 | 4 | 5 | 20 | Critical | Open | 164.312(e)(1) | Map and classify the flow as ePHI-bearing; verify TLS 1.2+ before further dispensing |
| EFC-003 | MFA disabled on nursing EHR accounts | IAC-06, IAC-02 | 5 | 4 | 20 | Critical | Open | 164.312(a)(2)(i) | Enforce MFA on all clinical accounts; audit login history for compromise |