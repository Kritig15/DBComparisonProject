import os
import subprocess
from send_email import send_email_report

import logging
send_email_report("reports/result_report.txt")
# Logging setup
logging.basicConfig(
    filename='logs/db_comparison.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# Run Behave tests
logging.info("Running behave tests...")
subprocess.run(["behave"], check=False)

# Email report
print("Sending email...")
send_email_report(
    sender_email="kritigupta003@gmail.com",
    sender_password="vaok ecok axzz wdtn",  # Use Gmail App Password
    recipient_email="kritigupta3389@gmail.com",
    report_path="reports/result_report.txt"
)
