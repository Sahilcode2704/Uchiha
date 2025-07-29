import pandas as pd
import requests
import time
from datetime import datetime, timedelta
import pytz
import csv
import os

# Load email function
try:
    code = requests.get("https://sahilcode2704.github.io/Uchiha/emailgrt.py").text
    print("📥 Code downloaded, running now:\n")
    exec(code)
except Exception as e:
    print("❌ Failed to download or run code:")
    print(e)

# Load contacts
contacts = pd.read_csv("https://sahilcode2704.github.io/Uchiha/contacts.csv")
print("✅ Contacts loaded")

# Set up log file
log_file = "email_log.csv"
log_fields = ["Name", "Email", "Time Sent", "Status"]
if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=log_fields)
        writer.writeheader()

# Schedule
target_ist = pytz.timezone('Asia/Kolkata').localize(
    datetime.now().replace(hour=14, minute=6, second=0, microsecond=0)
)
now_ist = datetime.now(pytz.timezone('Asia/Kolkata'))
if now_ist > target_ist:
    target_ist += timedelta(days=1)
wait_seconds = (target_ist - now_ist).total_seconds()
print(f"⏳ Waiting {int(wait_seconds)} seconds to send all emails at 7:00 PM IST...")
time.sleep(wait_seconds)

# Send and log
for index, row in contacts.iterrows():
    name = row["First Name"]
    email = row["Email"]

    subject = "Seeking Your Insight on Real-World Tech Challenges"
    message = f"""\
Dear {name},

I hope you're doing well. I'm reaching out as someone who is passionate about solving real-world problems through technology and AI.

I'm currently working on building meaningful projects and believe that the best ideas often come from actual challenges that professionals like you encounter — whether in architecture, development, data handling, system design, or daily operations.

If there's any issue, inefficiency, or idea you’ve come across — no matter how small — that you feel is worth exploring or solving, I would genuinely appreciate hearing about it. Your insight could help me work on something that brings real value.

Thank you for your time and the work you do. I'd be grateful for any advice or direction you’re willing to share.

Warm regards,  
Sahil N.  
sahiln27042008@gmail.com
"""

    try:
        emails(email, subject, message)
        status = "Sent"
        print(f"✅ Email sent to {name} ({email}) at {datetime.now().strftime('%H:%M:%S')}")
    except Exception as e:
        status = f"Failed: {e}"
        print(f"❌ Failed to send to {email}: {e}")

    with open(log_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=log_fields)
        writer.writerow({
            "Name": name,
            "Email": email,
            "Time Sent": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Status": status
        })