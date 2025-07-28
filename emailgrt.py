import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def emails(ine, msgx):
    # Configuration
    sender_email = "sahiln27042008@gmail.com"
    receiver_email = ine
    app_password = "feaylvqzmrfzaoil"  # 16-char app password
    subject = "Check Email"
    body = msgx

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

emails("sahiln27042008@gmail.com", "Dhfhydhdveeih")