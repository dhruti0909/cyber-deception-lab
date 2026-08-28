from pathlib import Path
log_file = Path("../logs/access.log")
score = 0
events = []
with open(log_file, "r") as log:
    for line in log:
        if"/admin" in line:
          score += 20
          events.append("Accessed decoy admin panel")
        if "DECOY:" in line:
            score += 40
            events.append("Accessed decoy credentials")
        if "backup" in line:
           score += 20
           events.append("Accessed backup path")
        if "credentials" in line:
           score += 20 
           events.append("Targeted credentials data")
        if "DECOY API:" in line:
           score += 30
           events.append("Accessed decoy API")
        if "404" in line:
           score += 5
           events.append("probed a non-existence endpoint")
score = min(score, 100)
if score >=70:
    risk = "HIGH"
elif score >= 40:
    risk = "MEDIUM"
else:
    risk = "LOW"
print("="* 40)
print("       CYBER DECEPTION LAB")
print("="* 40)
print(f"Threat Score : {score}/100")
print(f"Risk Level : {risk}")
print("\nDetected Events:")
if events:
     for event in set(events):
        print(f"- {event}")
else:
    print("No suspicious activity detected.")
print("=" * 45)
