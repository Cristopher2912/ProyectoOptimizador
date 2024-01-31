import threading
import time
import smtplib
import psutil
from email.mime.text import MIMEText
from datetime import datetime
import pytz

# Global lock for printing
print_lock = threading.Lock()

# IFTTT Email Address
ifttt_email = "trigger@applet.ifttt.com"

# Define the subject and body of the email
ifttt_subject = "CPU Usage Alert"
ifttt_body = "High CPU usage detected!"

# Function to send email
def send_email(subject, body):
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = ifttt_email
    message['To'] = ifttt_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("your_email@gmail.com", "your_password")
            server.sendmail(ifttt_email, ifttt_email, message.as_string())
        with print_lock:
            print("Email sent successfully.")
    except Exception as e:
        with print_lock:
            print(f"Error sending email: {e}")

# Function to monitor CPU usage
def monitor_cpu_usage():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        with print_lock:
            print(f'Current CPU Usage: {cpu_percent}%')
        # Check if CPU usage is above threshold and in Ecuador
        if cpu_percent > 0.1 and is_in_ecuador():
            send_email(ifttt_subject, ifttt_body)
        time.sleep(5)  # Check every 5 seconds

# Function to check if system is in Ecuador
def is_in_ecuador():
    # Get current time in Ecuador timezone
    ecuador_tz = pytz.timezone('America/Guayaquil')
    current_time = datetime.now(ecuador_tz)
    # Check if the current time is between 8 AM and 6 PM
    return 8 <= current_time.hour < 18

# Main function to start monitoring
if __name__ == "__main__":
    cpu_monitor_thread = threading.Thread(target=monitor_cpu_usage)
    cpu_monitor_thread.start()
