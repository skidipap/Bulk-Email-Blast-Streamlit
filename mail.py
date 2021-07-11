import yagmail 
from typing import List
import streamlit as st 

def send_mail(gmail: str, password: str, 
        recepients: List , subject: str, 
        content: str):
    
    """
        gmail : Gmail address of sender,
        password: Gmail Password / Token,
        recepient: List of Recepient,
        subject: Email Subject,
        content: Email Content,
    """
    st.write("Please Wait... Sending Emails.. In Progress")

    for recepient in recepients:
        with yagmail.SMTP(gmail, password) as yag: 
            yag.send(recepient, subject, content)
            print(f"Email Send To {recepient}")
            st.write(f"Email Send To {recepient}")
    
    st.write("All Email Completely Send")

