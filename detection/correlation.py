from pathlib import Path

log_file = Path("../logs/access.log")

recon = False
admin_access = False
credential_access = False

with open(log_file, "r") as log:
    for line in log:
        if "404 PROBE:" in line:
            recon = True

        if "Endpoint: /admin" in line:
            admin_access = True

        if "DECOY:" in line:
            credential_access = True

print("=" * 55)
print("           ATTACK BEHAVIOUR CORRELATION")
print("=" * 55)

print("\nObserved stages:")

if recon:
    print("[1] Reconnaissance detected")
if admin_access:
    print("[2] Decoy admin discovery detected")
if credential_access:
    print("[3] Credential targeting detected")

print("\nAttack Pattern:")

if recon and admin_access and credential_access:
    print("RECON → DISCOVERY → CREDENTIAL TARGETING")
    print("Assessment: HIGH CONFIDENCE ATTACK PATTERN")
elif recon and admin_access:
    print("RECON → DISCOVERY")
    print("Assessment: SUSPICIOUS")
elif admin_access or credential_access:
    print("DECOY INTERACTION DETECTED")
    print("Assessment: REQUIRES MONITORING")
else:
    print("No correlated attack pattern detected.")

print("=" * 55)
