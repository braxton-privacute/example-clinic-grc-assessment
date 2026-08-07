# Multi-Framework Coverage Report

Risk findings mapped across HIPAA Security Rule and NIST CSF 2.0 via the Secure Controls Framework (SCF) crosswalk. Coverage is measured against each framework as represented in the SCF crosswalk, not the full published framework.

## Coverage summary

| Framework | Controls covered | Total (in SCF) | Coverage |
|-----------|------------------|----------------|----------|
| HIPAA | 11 | 87 | 12.6% |
| NIST CSF | 16 | 134 | 11.9% |

## Findings and framework mappings

### EFC-001: Exfiltration of ePHI via vendor database

- **SCF controls:** TPM-02, TPM-05
- **HIPAA:** 164.308(a)(7)(ii)(E), 164.308(b)(1), 164.308(b)(2), 164.308(b)(3), 164.314(a)(2)(iii), 164.314(b)(1), 164.314(b)(2)(i), 164.314(b)(2)(ii), 164.314(b)(2)(iii)
- **NIST CSF:** GV.OC-04, GV.OC-05, GV.SC-04, GV.SC-06, GV.SC-07, GV.SC-08, ID.AM-05, ID.RA-10, GV.OC-02, GV.OC-03, GV.SC-02, GV.SC-05

### EFC-002: Unverified e-Rx data flow between EHR and pharmacy

- **SCF controls:** AST-02.8, CRY-03
- **HIPAA:** 164.312(e)(1)
- **NIST CSF:** PR.DS-02

### EFC-003: MFA disabled on nursing EHR accounts

- **SCF controls:** IAC-06, IAC-02
- **HIPAA:** 164.312(a)(2)(i)
- **NIST CSF:** PR.AA-01, PR.AA-03, PR.AA-05

## NIST CSF coverage by function

| Function | Subcategories covered | Status |
|----------|----------------------|--------|
| Govern | 10 | Covered |
| Identify | 2 | Covered |
| Protect | 4 | Covered |
| Detect | 0 | **No coverage** |
| Respond | 0 | **No coverage** |
| Recover | 0 | **No coverage** |

**Gap callout:** the assessment has no coverage in Detect, Respond, Recover. These functions represent the clearest next areas to assess.
