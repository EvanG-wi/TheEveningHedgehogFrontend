#streamlit web app daily goose

import json
import streamlit as st
import requests
import re

#THIS_DIR =Path(__file__).parent
#CSS_FILE + THIS_DIR / "style" / "style.css"
#ASSETS + THIS_DIR / "assets"

def send_request(email_address): #send http request with email to register a new account
    email_pattern = r"^\S+[@][a-z]+[.][a-z]{3}$"
    
    if not re.match(email_pattern,email_address):
        st.error("invalid email")
        return "invalid email"
    
    url = "https://us-central1-long-leaf-424918-h9.cloudfunctions.net/dailyGooseTestBuild"
    request_body = {
                     "task":"add_account",
                     "email_address":email_address,
                     "critter":"hedgehog"
                   }
    headers = {'Content-type': 'application/json'}
    
    response = requests.post(url,json = request_body, headers=headers)
    if response.status_code == 200:
        st.success(f"Request sent successfully")
        st.write("Congratulations!\nPlease remember to check your spam folder for communications from The Evening Hedgehog")
    else:
        st.error(f"Failed to send request. Status code: {response.status_code}")

#with open("style/style.css") as file:
    #st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

st.title("Subscribe to The Evening Hedghog")

email_address = st.text_input("Enter email address")

submit_button = st.button("Submit email address")



if submit_button:
    send_request(email_address)
    
    
st.image("hedge_img.png")    