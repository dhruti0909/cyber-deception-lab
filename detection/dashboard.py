from pathlib import Path

log_file = Path("../logs/access.log")

events = set()
score = 0

with open(log_file, "r") as log:
    for line in log:
        if "/admin" in line:
            events.add("Decoy admin accessed")
            score += 20

        if "DECOY:" in line:
            events.add("Decoy credentials accessed")
            score += 40

        if "DECOY API:" in line:
            events.add("Decoy API accessed")
            score += 30

        if "404" in line:
            events.add("Non-existent endpoint probed")
            score += 5

score = min(score, 100)

if score >= 70:
    risk = "HIGH"
elif score >= 40:
    risk = "MEDIUM"
else:
    risk = "LOW"

print("=" * 55)
print("             CYBER DECEPTION LAB")
print("                SECURITY DASHBOARD")
print("=" * 55)

print(f"\nThreat Score : {score}/100")
print(f"Risk Level   : {risk}")

print("\nDetected Activity:")

if events:
    for event in sorted(events):
        print(f"- {event}")
else:
    print("- No suspicious activity")

print("\nAttack Assessment:")

if "Decoy admin accessed" in events and "Decoy credentials accessed" in events:
    print("Credential-targeting behaviour detected.")

if "Non-existent endpoint probed" in events:
    print("Reconnaissance behaviour detected.")

if "Decoy API accessed" in events:
    print("API discovery behaviour detected.")

print("=" * 55)
