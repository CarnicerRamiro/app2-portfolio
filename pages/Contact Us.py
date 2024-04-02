import streamlit as st
from send_email import send_email

st.header("Contact Me!")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Confirm")
    if button:
        message_to_send = f"""\
Subject: automated email from {user_email}

From: {user_email}
{message}
"""
        send_email(message_to_send)
        st.info("Your email has been sent")
