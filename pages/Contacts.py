import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Us")
df = pandas.read_csv("topics.csv")

with st.form(key="email_from"):
    user_email = st.text_input("Your email address")
    selected_topic = st.selectbox(
        "What topic do you want to discuss?",
        df["topic"])
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Email from Best Company app

Topic: {selected_topic}
From: {user_email}
{raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
