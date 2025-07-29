import pandas as pd
import requests
import time
from datetime import datetime, timedelta
import pytz
import csv
import os
import logging

# === CONFIG ===
EMAIL_FUNCTION_URL = "https://sahilcode2704.github.io/Uchiha/emailgrt.py"
CONTACTS_CSV_URL = "https://sahilcode2704.github.io/Uchiha/contacts.csv"
LOG_FILE = "email_log.csv"
SEND_HOUR = 19  # Default scheduled time (7:00 PM IST)
SEND_MINUTE = 0

# === SETUP LOGGING ===
logging.basicConfig(filename="email_errors.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# === LOAD EMAIL FUNCTION ===
def load_email_function(url):
    try:
        code = requests.get(url).text
        print("📥 Code downloaded, running now:\n")
        exec(code, globals())
        if 'emails' not in globals():
            raise ValueError("Function 'emails' not found in downloaded code.")
    except Exception as e:
        print("❌ Failed to download or run email function:")
        print(e)
        logging.error(f"Error loading email function: {e}")
        exit(1)

load_email_function(EMAIL_FUNCTION_URL)

# === LOAD CONTACTS ===
try:
    contacts = pd.read_csv(CONTACTS_CSV_URL)
    print("✅ Contacts loaded")
except Exception as e:
    print("❌ Failed to load contacts CSV:")
    print(e)
    logging.error(f"Error loading contacts: {e}")
    exit(1)

# === SET UP LOG FILE ===
log_fields = ["Name", "Email", "Time Sent", "Status"]
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=log_fields)
        writer.writeheader()

# === ASK USER TO SCHEDULE OR SEND NOW ===
choice = input("⏱ Do you want to schedule the emails for 7:00 PM IST? (y/n): ").strip().lower()

if choice == 'y':
    timezone = pytz.timezone('Asia/Kolkata')
    now = datetime.now(timezone)
    target_time = timezone.localize(now.replace(hour=SEND_HOUR, minute=SEND_MINUTE, second=0, microsecond=0))

    if now > target_time:
        target_time += timedelta(days=1)

    wait_seconds = int((target_time - now).total_seconds())
    print(f"⏳ Waiting until {target_time.strftime('%Y-%m-%d %H:%M:%S %Z')} to send emails...")

    while wait_seconds > 0:
        hrs, rem = divmod(wait_seconds, 3600)
        mins, secs = divmod(rem, 60)
        print(f"⏳ Time remaining: {hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
        time.sleep(min(30, wait_seconds))
        wait_seconds -= 30

    if wait_seconds > 0:
        time.sleep(wait_seconds)
else:
    print("🚀 Sending emails now without waiting...")

# === SEND EMAILS & LOG ===
with open(LOG_FILE, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=log_fields)
    for index, row in contacts.iterrows():
        name = row.get("First Name", "User")
        email = row.get("Email", "").strip()

        subject = "Seeking Your Insight on Real-World Tech Challenges"
        message = f"""\
Dear {name},

I hope you're doing well. I'm reaching out as someone who is passionate about solving real-world problems through technology and AI.

I'm currently working on building meaningful projects and believe that the best ideas often come from actual challenges that professionals like you encounter — whether in architecture, development, data handling, system design, or daily operations.

If there's any issue, inefficiency, or idea you’ve come across — no matter how small — that you feel is worth exploring or solving, I would genuinely appreciate hearing about it. Your insight could help me work on something that brings real value.

Thank you for your time and the work you do. I'd be grateful for any advice or direction you’re willing to share.

Warm regards,  
Sahil 
sahiln27042008@gmail.com
"""

        try:
            emails(email, subject, message)
            status = "Sent"
            print(f"✅ Email sent to {name} ({email}) at {datetime.now().strftime('%H:%M:%S')}")
        except Exception as e:
            status = f"Failed: {e}"
            print(f"❌ Failed to send to {email}: {e}")
            logging.error(f"Failed to send to {email}: {e}")

        writer.writerow({
            "Name": name,
            "Email": email,
            "Time Sent": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Status": status
        })