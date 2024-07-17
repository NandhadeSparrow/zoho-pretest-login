import streamlit as st
from util import auth
from pages import login, profile, register

# login.login()
# register.register()
if profile.profile() == 'login':
    st.switch_page("pages/login.py")

