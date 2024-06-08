#Send Request

import re
import requests
import json
import streamlit as st

def send_request(email_address, critter): #send http request with email to register a new account
    email_pattern = r"^\S+[@][a-z]+[.][a-z]{3}$"
    
    if not re.match(email_pattern,email_address):
        st.error("invalid email")
        return "invalid email"
    
    url = "https://us-central1-long-leaf-424918-h9.cloudfunctions.net/dailyGooseTestBuild"
    request_body = {
                     "task":"add_account",
                     "email_address":email_address,
                     "critter":critter
                   }
    headers = {'Content-type': 'application/json'}
    
    response = requests.post(url,json = request_body, headers=headers)
    if response.status_code == 200:
        st.success(f"Request sent successfully. \nCongratulations!\nPlease remember to check your spam folder for communications from The Daily Goose")
    else:
        st.error(f"Failed to send request. Status code: {response.status_code}")