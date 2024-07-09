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

# Schedule the function
schedule.every(1).minutes.do(my_scheduled_function)

# Function to run the scheduler
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

# To keep Streamlit app responsive and running
if 'initialized' not in st.session_state:
    st.session_state.initialized = True

st.write("Scheduler is running in the background.")
