from send_email import send_email_report
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch values from .env
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Call the email function
send_email_report(
    sender_email=SENDER_EMAIL,
    sender_password=SENDER_PASSWORD,
    recipient_email=RECIPIENT_EMAIL,
    report_path="reports/result_report.txt"
)
