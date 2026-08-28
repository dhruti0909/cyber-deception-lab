from pathlib import Path
log_file = Path("../logs/access.log")
print("=" * 60)
print("         ATTACK TIMELINE")
print("="* 60)
with open(log_file, "r") as log:
   for line in log:
       parts = line.strip().split(" | ")
       if len(parts) >= 3:
          timestamp = parts[0]
          ip = parts[1].replace("IP: ","")
          action = parts[2]
          print(f"{timestamp} | {ip} | {action}")
print("="* 60)

