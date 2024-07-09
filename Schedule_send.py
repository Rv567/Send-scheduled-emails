import streamlit as st
import schedule
import time
from datetime import datetime
import threading
from send_function import send_email

# Streamlit app code
st.title("My Streamlit App with Scheduler")
st.write("The function will send emails every 1 minute")

# Your function to be scheduled
def my_scheduled_function():
    send_email(sender_email="rachid.chentouf71@gmail.com",
               receiver_email="rachid.axiom@gmail.com",
               subject='Test Email',
               body='This is a test email sent from Python!',
               smtp_server='smtp.gmail.com',
               smtp_port=587,
               app_password='foicfxiwfxwirtjb')
    st.write(f"Email sent at : {datetime.now()}")

# Function to run the scheduler
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Schedule the function
schedule.every(1).minute.do(my_scheduled_function)

# Run the scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

# Streamlit loop to keep the app running
while True:
    time.sleep(1)
