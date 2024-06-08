#streamlit web app daily goose

import streamlit as st
from send_request import send_request
from streamlit_option_menu import option_menu

with open("style/style.css") as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

critter_select = option_menu(
                             menu_title=None,
                             options=["The Daily Goose","The Evening Hedgehog"],
                             orientation="horizontal"
                            )


st.title("Subscribe to "+critter_select)

email_address = st.text_input("Enter email address")

submit_button = st.button("Submit email address")

if submit_button:
    if critter_select=="The Daily Goose":
        send_request(email_address,"goose")
    elif critter_select=="The Evening Hedgehog":
        send_request(email_address,"hedgehog")

if critter_select=="The Daily Goose":
    st.image("ottomanEmpireCourtGoose.png")
elif critter_select=="The Evening Hedgehog":
    st.image("hedge_img.png")    