import streamlit as st
from util import auth

def login():
    st.markdown('## Login')

    st.text_input('Username', value="", key='username-login')
    st.text_input('Password', value="", key='password-login')
    if st.button('LogIn', key='login', type="secondary"):
        if auth.login():
            return 'profile'
        else:
            st.error('Login Error')

if __name__ == '__main__':
    st.session_state['page'] = 'login'
    login()