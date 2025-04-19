import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter Your E-mail", placeholder="Your E-mail")
    raw_user_message = st.text_area("Enter Your Message", placeholder="Your Queries or Messages")
    user_message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_user_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_message)
        st.info("Email Sent Sucessfully..!")