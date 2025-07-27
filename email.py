import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
receiver_email = "sahilgrt426@gmail.com"
app_password = "feaylvqzmrfzaoil"  # 16-char app password
sender_email = "sahiln27042008@gmail.com"
subject = "Test Email Without Gmail API"
body = "Hello, this is a test email sent using Python and SMTP."

# Compose email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send email via Gmail SMTP
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error sending email:", e)