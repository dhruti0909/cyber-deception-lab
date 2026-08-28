from pathlib import Path
from datetime import datetime

log_file = Path("../logs/access.log")

events = []

with open(log_file, "r") as log:
    for line in log:
        if "/admin" in line:
            events.append("Decoy admin panel accessed")

        if "DECOY:" in line:
            events.append("Decoy credentials accessed")

        if "404 PROBE:" in line:
            events.append("Non-existent endpoint probed")

print("=" * 60)
print("              CYBER DECEPTION LAB")
print("                 ATTACK REPORT")
print("=" * 60)

print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

print("TOTAL EVENTS:", len(events))
print()

print("OBSERVED BEHAVIOUR:")

if events:
    for event in sorted(set(events)):
        print(f"- {event}")
else:
    print("- No suspicious activity detected")

print()
print("RECOMMENDATION:")

if len(events) >= 3:
    print("- HIGH PRIORITY: Investigate the source activity.")
elif len(events) >= 1:
    print("- Monitor the activity for further suspicious behaviour.")
else:
    print("- Continue monitoring.")

print("=" * 60)
