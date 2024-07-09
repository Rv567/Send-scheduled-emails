import streamlit as st
import schedule
import time
from datetime import datetime
from send_function import *


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
    #st.write(f"Email sent at : {datetime.now()}")
   

schedule.every(1).minutes.do(my_scheduled_function)

# Function to run the scheduler
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

run_scheduler()


