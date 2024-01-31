import threading
import time
import smtplib
import psutil
from email.mime.text import MIMEText

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
        # Check if CPU usage is above threshold and in specific zone
        if cpu_percent > 0.1 and is_in_specific_zone():
            send_email(ifttt_subject, ifttt_body)
        time.sleep(5)  # Check every 5 seconds

# Function to check if CPU usage is in a specific zone
def is_in_specific_zone():
    # Add your logic to determine if CPU usage is in specific zone
    # For example, you can check if the current time is within a certain range
    # or if the CPU usage is above a certain threshold
    return True  # Modify this condition based on your requirement

# Main function to start monitoring
if __name__ == "__main__":
    cpu_monitor_thread = threading.Thread(target=monitor_cpu_usage)
    cpu_monitor_thread.start()

