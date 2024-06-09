#streamlit web app daily goose

import streamlit as st
from send_request import send_request
from streamlit_option_menu import option_menu

st.set_page_config(page_title="The Daily Goose",page_icon=':duck:')#browser tab

with open("style/style.css") as file:#remove streamlit default header and fix spacing
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)
    
def click_button():
    if critter_select=="The Daily Goose":
        send_request(email_address,"goose")
    elif critter_select=="The Evening Hedgehog":
        send_request(email_address,"hedgehog")  
    st.session_state['email'] = ""



#Page Elements###
critter_select = option_menu(
                             menu_title=None,
                             options=["The Daily Goose","The Evening Hedgehog"],
                             orientation="horizontal"
                            )
st.title("Subscribe to "+critter_select)

email_address = st.text_input("Enter email address",key='email')

submit_button = st.button("Submit email address", on_click=click_button)
################

if critter_select=="The Daily Goose":
    st.image("ottomanEmpireCourtGoose.png")
elif critter_select=="The Evening Hedgehog":
    st.image("hedge_img.png")