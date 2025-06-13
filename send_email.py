import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging

# Logging setup
logging.basicConfig(
    filename='logs/db_comparison.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_email_report(sender_email, sender_password, recipient_email, report_path):
    try:
        with open(report_path, 'r', encoding='utf-8') as file:
            report_content = file.read()

        msg = MIMEText(report_content, 'plain', 'utf-8')
        msg['Subject'] = Header('DB Comparison Report', 'utf-8')
        msg['From'] = sender_email
        msg['To'] = recipient_email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        logging.info("✅ Email sent successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to send email: {e}")
