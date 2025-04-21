import time
from collections import defaultdict

LOG_FILE = "simulated_auth.log"
THRESHOLD = 5  # max failed attempts before alert
TIME_WINDOW = 60  # seconds

# Track failed attempts: {ip: [timestamps]}
failed_attempts = defaultdict(list)

def monitor_logs():
    print("🔍 Monitoring log for suspicious activity...\n")
    with open(LOG_FILE, "r") as file:
        # Jump to end of file
        file.seek(0, 2)

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue

            process_log_line(line.strip())

def process_log_line(line):
    if "Failed password" in line:
        parts = line.split()
        ip = parts[-1]  # assume IP is at end
        timestamp = time.time()

        failed_attempts[ip].append(timestamp)

        # Remove old timestamps
        failed_attempts[ip] = [t for t in failed_attempts[ip] if timestamp - t <= TIME_WINDOW]

        if len(failed_attempts[ip]) >= THRESHOLD:
            print(f"🚨 ALERT: {len(failed_attempts[ip])} failed attempts from {ip} within {TIME_WINDOW} seconds!")

if __name__ == "__main__":
    monitor_logs()
