import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from dotenv import load_dotenv

# ✅ Load environment variables only if NOT running in GitHub Actions
if os.environ.get("GITHUB_ACTIONS") != "true":
    load_dotenv()

# ✅ Match with GitHub Secrets and .env keys
SENDER_EMAIL = os.getenv("EMAIL_USERNAME")
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("EMAIL_RECIPIENT")

# Logging setup
logging.basicConfig(
    filename='logs/db_comparison.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_email_report(report_path, log_path='logs/db_comparison.log'):
    try:
        # Read report content
        with open(report_path, 'r', encoding='utf-8') as file:
            report_content = file.read()

        # Create a multipart message
        msg = MIMEMultipart()
        msg['Subject'] = Header('📊 DB Comparison Report', 'utf-8')
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL

        # Add report content as email body
        body = MIMEText(report_content, 'plain', 'utf-8')
        msg.attach(body)

        # Attach the log file
        with open(log_path, 'rb') as f:
            log_attachment = MIMEApplication(f.read(), _subtype="txt")
            log_attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(log_path))
            msg.attach(log_attachment)

        # Send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        logging.info("✅ Email sent successfully with log attachment.")

    except Exception as e:
        logging.error(f"❌ Failed to send email: {e}")
