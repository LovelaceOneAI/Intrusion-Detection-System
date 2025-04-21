# Simple IDS

A basic Python intrusion detection system (IDS) that monitors logs and raises alerts when suspicious activity is detected—like repeated failed login attempts from the same IP.

## 🛠 How It Works

- Watches a log file (`simulated_auth.log`) in real time
- Detects brute-force-style login failures
- Alerts when 5+ failed logins from the same IP occur within 60 seconds

## ▶️ How to Run

1. Clone this repo
2. Open a terminal and run:

```bash
python simple_ids.py
